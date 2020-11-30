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
| pts1/step_size | One of SINGLE, DOUBLE, INTERLEAVED, or MICROSTEP | How big each step is |
| pts1/step_delay | (number) | ms delay between steps.  Defaults to zero.  |
| pts1/pan/cw | int: num steps | Moves pan stepper the specified number of steps clockwise |
| pts1/pan/ccw | int num steps | Moves pan stepper the specified number of steps counter-clockwise |
| pts1/tilt/up | int: num steps | Moves the tilt stepper the specifed number of steps up |
| pts1/tilt/down | int: num steps| Moves the tilt stepper the specified number of steps down |
| pts1/stop | none | stops any in motion progress |
| pts1/release | none | stops any motion and releases stepper coils |

## Pi stepper driver
"StepperMotion" object type contains:
* a pointer to the stepper driver from the adafruit "MotorKit" object
* a flag telling whether we are moving or not.
* Which direction are we going (stepper.FORWARD or stepper.BACKWARD)
* step size
* step delay
* if we're moving:
  * how many steps do we need to take?
  * how many steps have we already taken?
  * when do we need to take our next step?
  
MQTT callback sets all of these...one global for pan, one for tilt.

Object has a driver function:
* what time is it now?
* if the stepper has more to go, is it time for a pan step?  If so, do it.

"Main" initializes MQTT, creates our pan and tilt objects, then does a try/except loop calling the driver function.  ctl-c exits.

## TK interface
coming later...will start testing with mqtt_sniffer
