#!/usr/bin/env python3
"""Extract an Arduino sketch from the most recent email (.eml) in ~/Downloads.

Run from inside the Arduino sketch folder. The sketch is written to
./PicoAiBotDownloadedSketch/PicoAiBotDownloadedSketch.ino, and you are
offered the option to compile and upload it to the Pico.

The HTML part of the email is preferred because mail clients hard-wrap the
plain-text part, which breaks long code lines.
"""

import email
import email.policy
import json
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

SKETCH_NAME = "PicoAiBotDownloadedSketch"
DOWNLOADS = Path.home() / "Downloads"
FQBN = "rp2040:rp2040:rpipico"
DEFAULT_PORT = "/dev/ttyACM0"

BLOCK_TAGS = {"div", "p", "pre", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}


class HtmlToText(HTMLParser):
    """Convert simple email HTML to text, turning <br> and block tags into newlines."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def _ensure_newline(self):
        if self.parts and not self.parts[-1].endswith("\n"):
            self.parts.append("\n")

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.parts.append("\n")
        elif tag in BLOCK_TAGS:
            self._ensure_newline()

    def handle_endtag(self, tag):
        if tag in BLOCK_TAGS:
            self._ensure_newline()

    def handle_data(self, data):
        self.parts.append(data)

    def text(self):
        return "".join(self.parts)


def ask(prompt, default="n"):
    suffix = " [Y/n] " if default == "y" else " [y/N] "
    try:
        reply = input(prompt + suffix).strip().lower()
    except EOFError:
        reply = ""
    return (reply or default).startswith("y")


def newest_download():
    files = [p for p in DOWNLOADS.iterdir() if p.is_file() and not p.name.startswith(".")]
    if not files:
        sys.exit(f"No files found in {DOWNLOADS}")
    return max(files, key=lambda p: p.stat().st_mtime)


def extract_sketch(eml_path):
    with open(eml_path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=email.policy.default)

    html_part = msg.get_body(preferencelist=("html",))
    if html_part is not None:
        parser = HtmlToText()
        parser.feed(html_part.get_content())
        text = parser.text()
    else:
        plain_part = msg.get_body(preferencelist=("plain",))
        if plain_part is None:
            sys.exit(f"No text or HTML body found in {eml_path.name}")
        print("Warning: no HTML part; using plain text, which may have wrapped lines.")
        text = plain_part.get_content()

    # Gmail indents with non-breaking spaces; the compiler needs real ones.
    text = text.replace(" ", " ")
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(lines).strip("\n") + "\n"


def detect_port():
    """Return the port of the first connected RP2040 board, or None."""
    try:
        out = subprocess.run(["arduino-cli", "board", "list", "--format", "json"],
                             capture_output=True, text=True, check=True).stdout
        for entry in json.loads(out).get("detected_ports", []):
            for board in entry.get("matching_boards", []):
                if board.get("fqbn", "").startswith("rp2040:"):
                    return entry["port"]["address"]
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError, KeyError):
        pass
    return None


def main():
    source = newest_download()
    print(f"Most recent file in {DOWNLOADS}:\n  {source.name}")
    if not ask("Extract the Arduino sketch from this file?"):
        sys.exit("Cancelled.")

    sketch = extract_sketch(source)

    sketch_dir = Path.cwd() / SKETCH_NAME
    sketch_dir.mkdir(exist_ok=True)
    ino = sketch_dir / f"{SKETCH_NAME}.ino"
    if ino.exists():
        backup = ino.with_suffix(".ino.bak")
        shutil.copy2(ino, backup)
        print(f"Backed up existing sketch to {backup}")
    ino.write_text(sketch)
    print(f"Wrote {ino} ({len(sketch.splitlines())} lines)")

    if not ask("Compile and upload to the Pico now?"):
        return

    port = detect_port() or DEFAULT_PORT
    try:
        entered = input(f"Port [{port}]: ").strip()
    except EOFError:
        entered = ""
    port = entered or port

    cmd = ["arduino-cli", "compile", "-u", "-p", port, "--fqbn", FQBN, str(sketch_dir)]
    print("Running:", " ".join(cmd))
    sys.exit(subprocess.run(cmd).returncode)


if __name__ == "__main__":
    main()
