Workshop Content
================

# Theory

## Workflow
- Workflow diagram showing instructions given to AI, AI prints code, user copies
code into Arduino IDE, and uses IDE to program Arduino. Arduino gets mounted onto
robot and operates it.

## Arduino + Robot Overview
- Define Arduino as meaning a microcontroller that runs firmware in the Arduino environment
  - what is the Arduino environment: setup() and loop(0) functions, plus Arduino language
- Diagram showing arduino with two pins driving switches which control 2 motors on robot
- Explain The Challenge, and how your firware will drive the motors (forwards-only) to
accomplish the goal.

## PWM for motor speed control

- Diagram showing pulsed voltage applied to motor. Diagram to include 10% and 90% PWM pulses
- Motor speed is related to average duration of applied power

## How to use AI (demo)

- Launch google in AI mode
- Give it a detailed instruction on what to do, with context. Example:

> I have an LED controlled by PWM on GP0. Give me an arduino sketch
> to ramp it up to full brightness then back down to off every 5 seconds

- Copy the resuling sketch into the Arduino IDE

### Next level (not this workshop):
- run AI in your machine to directly edit files (antigravity), Claude, OpenAI Codex

> I have an LED controlled by PWM on GP0. Write a file called led_ramp.ino
> in the current directory which is an arduino sketch
> to ramp it up to full brightness then back down to off every 5 seconds

# Practical

## Laptop pre-checks
- Make sure everyone can connect to guest wifi
- Check everyone has pre-loaded Arduino

## Load Pico support into Arduino IDE

Steps shown with screen captures

## Connect Arduino and test example

- Connect Arduino to laptop
- Launch Arduino IDE and open blink example
- Build and program blink example. Observe flashing LED

## Ask AI to write a sketch

- Open up google in AI mode. Give it the following instruction:

> I have a differential drive robot with two motors controlled by PWM.
> The left motor is driven by GP0. The right motor is driven by GP1.
> Give me an arduino sketch to ramp it up to full speed then back down to stopped every 5 seconds
