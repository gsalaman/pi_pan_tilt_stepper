# pi_pan_tilt_stepper
This repo uses the pi's stepper bonnet to control two stepper motors, via MQTT.

## Requirements
Want to do the following over MQTT:
* Step pan cw or ccw a certain number of steps
* Step tilt up or down a certian number of steps
* Set step size:  full, half, micro
* Set delay between steps
* Stop any step motion in action
* release stepper motor

## High level architecture
* pan/tilt assembly, 3d printed with parts from servocity and 2 stepper motors
* raspberry pi to host MQTT broker and control steppers (through python)
* python TK app to act as UI.

## MQTT Interface
coming first...

## Pi stepper driver
coming next...

## TK interface
coming later...
