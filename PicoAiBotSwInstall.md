# Install Pico AI Bot Software

Rev 0.1 10/13/26

This document explains how to load the Arduino IDE and Raspberry Pi Pico support onto your laptop **before** the workshop. Please do this at home: the Pico support is a large download (several hundred MB) and the workshop wifi can't handle ten people downloading it at once.

Allow about 30 minutes. You do **not** need a Pico to do this. Step 4 checks that everything works without any hardware.

If you get stuck, email [paul.bouchier@gmail.com](mailto:paul.bouchier@gmail.com) before the workshop.

# Step 1: Install the Arduino IDE (version 2.x)

Download the latest Arduino IDE 2.x for your operating system from [https\://www\.arduino.cc/en/software/\#ide](https://www.arduino.cc/en/software/#ide)

You don't have to donate or sign up; click "Just Download".

## Windows (10 or newer)

- Download the Windows installer (.exe) and run it. Accept the defaults.  
- If Windows asks whether to install drivers from Arduino, say **Yes/Install**.

## macOS (Monterey or newer)

- Download the .dmg file for your Mac's processor: Apple Silicon (M1/M2/M3/M4) or Intel. If you're not sure, check Apple menu \> About This Mac.  
- Open the .dmg and drag Arduino IDE into Applications.  
- The first time you launch it, macOS may warn that it was downloaded from the internet. Click **Open**.

## Linux

- Download the AppImage (64-bit) file.  
- Make it executable and run it:

chmod \+x arduino-ide\_\*.AppImage

./arduino-ide\_\*.AppImage

- If it won't start on Ubuntu 22.04 or newer, install FUSE: `sudo apt install libfuse2` (on Ubuntu 24.04 the package is `libfuse2t64`).  
- Give yourself permission to use serial ports, then **log out and back in**:

sudo usermod \-aG dialout \$USER

## First launch

Start the Arduino IDE once while connected to the internet. On first launch it downloads some extra components. Let it finish, and allow any firewall or driver prompts.

# Step 2: Tell Arduino where to find Pico support

1. Open the Preferences window:  
   - Windows/Linux: **File \> Preferences**  
   - macOS: **Arduino IDE \> Settings**  
2. Find the box labeled **Additional boards manager URLs** and paste in this URL:

https\://github.com/earlephilhower/arduino-pico/releases/download/global/package\_rp2040\_index.json

3. Click **OK**.

If there's already a URL in that box, click the icon next to it and add this one on a new line.

# Step 3: Install the Pico board package

1. Open the Boards Manager: **Tools \> Board \> Boards Manager...** (or click the board icon in the left sidebar).  
2. Type **pico** in the search box.  
3. Find **Raspberry Pi Pico/RP2040/RP2350** by **Earle F. Philhower, III** and click **Install**.  
   - **Don't** install "Arduino Mbed OS RP2040 Boards". That's a different Pico package, and it isn't the one we'll use.  
4. Wait for it to finish. This is the large download and can take several minutes. The output panel at the bottom shows progress.

# Step 4: Check it works (no Pico needed)

1. Select the board: **Tools \> Board \> Raspberry Pi Pico/RP2040/RP2350 \> Raspberry Pi Pico**  
2. Open the Blink example: **File \> Examples \> 01.Basics \> Blink**  
3. Click the **Verify** button (the check mark at top left).  
4. The first build is slow. When it finishes, the output panel should end with something like:

Sketch uses 52345 bytes (2%) of program storage space...

If you see that, you're ready for the workshop. You don't need to upload anything; there's no Pico connected.

# At the workshop: first upload to a Pico

This is covered in the workshop. It's here for reference.

1. Plug the Pico into your laptop with the USB cable.  
2. Under **Tools \> Port**, select the Pico's port. On a brand-new Pico it may show up as **UF2 Board**; after the first upload it shows up as a serial port (COMx on Windows, /dev/ttyACM0 on Linux, /dev/cu.usbmodem... on macOS).  
3. Click **Upload** (the right-arrow button).  
4. If no port appears, or the upload fails: unplug the Pico, **hold down the white BOOTSEL button** on the Pico while plugging it back in, then release it. It will appear as a USB drive called RPI-RP2. Select the UF2 Board port and upload again.

# Troubleshooting

- **The Raspberry Pi Pico boards don't appear in the Boards Manager search.** Check the URL in Step 2 is exactly right (no spaces), then close and reopen the IDE.  
- **The board package download fails or stalls.** Retry. If you're on a work or school network, try a home network. Antivirus software sometimes blocks the download, so try pausing it temporarily.  
- **Verify fails with an error.** Make sure the selected board (bottom right of the IDE window, or Tools \> Board) is Raspberry Pi Pico. Copy the error message and email it to [paul.bouchier@gmail.com](mailto:paul.bouchier@gmail.com).  
- **Linux: upload fails with "permission denied".** You need to be in the `dialout` group (see Step 1\) and you must log out and back in after adding yourself.  
- More help: [https\://arduino-pico.readthedocs.io/en/latest/install.html](https://arduino-pico.readthedocs.io/en/latest/install.html)