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
| Topic | Payload | Description |
| ----- | ------- | ----------- |
| pts1/step_size | (number) | One of SINGLE, DOUBLE, INTERLEAVED, or MICROSTEP |
| pts1/step_delay | (number) | ms delay between steps.  Defaults to zero.  |
| pts1/pan/cw | int: num steps | Moves... |
| pts1/pan/ccw | int num steps | moves... |
| pts1/tilt/up | | |
| pts1/tilt/down | | |
| pts1/stop | none | stops any in motion progress |
| pts1/release | none | stops any motion and releases stepper coils |


## Pi stepper driver
"motion" object type (use one for pan and one for tilt).
  contains step size
  contains ...
Main loop driver keeps track of which motion(s) are active, how many steps we need to take in each motion, and timestamp for the next step.

If it's time to take a step, use the driver to "onestep()" it.

MQTT callback sets:
* 

## TK interface
coming later...
