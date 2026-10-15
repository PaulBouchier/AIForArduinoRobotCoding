# Pico AI Bot Content Summary

# Theory

## Workflow

- Workflow diagram showing instructions given to AI, AI prints code, user copies
  code into Arduino IDE, and uses IDE to program Arduino. Arduino gets mounted onto robot and operates it.

## Arduino \+ Robot Overview

- Define Arduino as meaning a microcontroller that runs firmware in the Arduino environment
  - The Arduino environment: setup() and loop() functions, plus Arduino language
- Diagram showing arduino with two pins driving PNP transistors on hight side of 2 motors on robot. Beside transistors, draw a switch symbol
- 
- Explain The Challenge, and how your firmware will drive the motors (forwards-only) to accomplish the goal.

## PWM for motor speed control

- Diagram showing pulsed voltage applied to motor. Diagram to include 10% and 90% PWM pulses
- Motor speed is related to average duration of applied power
- analogWrite defaults to a 0–255 range on this core, so a duty cycle like 50% becomes about 128

## How to use AI (demo)

- Launch google in AI mode
- Give it a detailed instruction on what to do, with context. Example:

> I have an LED controlled by PWM on GP0 on a Raspberry Pi Pico. I am using the Arduino IDE with the earlephilhower arduino-pico core.. Give me an arduino sketch to ramp it up to full brightness then back down to off every 5 seconds  

- Copy the resulting sketch into the Arduino IDE. Download & show.
- Note this is not a great instruction \- it's ambiguous regarding whether the ramp should take 5 seconds or the loop should take 5 seconds. The AI will take a guess.

### Next level (not this workshop):

- run AI in your machine to directly edit files (Google Antigravity, Claude Code, OpenAI Codex, GitHub Copilot, Cursor)

> I have an LED controlled by PWM on GP0. Write a file called led\_ramp.ino in the current directory which is an arduino sketch to ramp it up to full brightness then back down to off every 5 seconds

# Hands-on

## Laptop pre-checks

- Make sure everyone can connect to guest wifi and access Google in AI mode
- Check everyone has pre-loaded Arduino IDE and Pico support
- If you haven't already loaded Arduino and Pico software, **Please don't try** - you will ruin the class for everyone by hogging DMS wifi bandwidth.

## Connect Arduino and test example

- Connect Pico to laptop
- Launch Arduino IDE and open blink example
- Set the board type (Pico) and port (e.g. /dev/ttyACM0, COM9)  
- Build and program blink example. Observe flashing LED

## Ask AI to write a sketch

- Open up google in AI mode. Give it the following instruction:

> I have a differential drive robot with two motors controlled by PWM. The PWM signal is produced by a Raspberry Pi Pico. I am using the Arduino IDE with the earlephilhower arduino-pico core. The left motor is driven by GP1. The right motor is driven by GP0. The GPIO pins drive a PNP transistor that enables the motors. When the output is low (PWM \= 0%) the motors run at full speed. When the output is high (PWM \= 100%) the motors are stopped. Give me an arduino sketch to control the motors as follows. The motors should be stopped for 5 seconds at startup. Then the left motor should ramp to full speed in 1 second then ramp down to stopped in 1 second. Then the right motor should ramp to full speed in 2 seconds, run at full speed for 1 second, then ramp down to stopped in 1 second. Then the sequence should repeat twice after which the motors should stay stopped.   

- Copy the code it produces into the Arduino IDE. Set the board type to Raspberry Pi Pico, and build and load the sketch into the Raspberry Pi  

- Look at the LEDs and check that the light pattern is as specified. If results aren't as expected, ask AI to add debug print statements to the sketch. Load the modified sketch and watch the prints with the Arduino monitor. Look at the code. Ask AI how the code works.  

- Put your interposer on a robot. Get the wheels off the ground and check that the wheels move as expected. Put the robot on the table and check it spins one way then the other.

## The Challenges

### Robot Motion

Make a robot do the best break-dancing moves. Get AI to write code that makes the robot move in fun and interesting ways. Spins and herky-jerky is good. It should begin its moves upon power on, and stop when its finished.

### Winky-Blinky

Make a 2-LED interposer board do the most fun blinky-light pattern

### How-To

- Begin by writing a plan in plain English first (e.g. forward 2 seconds at 50%, pause 0.5 sec, .....). Then paste your plan into the prompt with the surrounding context (pin numbers etc).

Prez Mark will judge the best performances. There is no prize \- maybe a certificate
