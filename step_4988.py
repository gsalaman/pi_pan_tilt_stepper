##########
# 4988 Stepper driver 
##########
import RPi.GPIO as GPIO
import time

# Hardcoded pin definitions for now.   Will eventually specifiy in constructor
m1_pin = 11
m2_pin = 13
m3_pin = 15
step_pin = 19 
dir_pin = 21
enable_pin = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(m1_pin, GPIO.OUT)
GPIO.setup(m2_pin, GPIO.OUT)
GPIO.setup(m3_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)

# step_size is 1, 2, 4, 8, or 16...so 16 = "sixteenth" steps. 
def set_step_size(step_size):
  if (step_size == 1):
    GPIO.output(m1_pin, GPIO.LOW)
    GPIO.output(m2_pin, GPIO.LOW)
    GPIO.output(m3_pin, GPIO.LOW)
  elif (step_size == 2):
    GPIO.output(m1_pin, GPIO.HIGH)
    GPIO.output(m2_pin, GPIO.LOW)
    GPIO.output(m3_pin, GPIO.LOW)
  elif (step_size == 4):
    GPIO.output(m1_pin, GPIO.LOW)
    GPIO.output(m2_pin, GPIO.HIGH)
    GPIO.output(m3_pin, GPIO.LOW)
  elif (step_size == 8):
    GPIO.output(m1_pin, GPIO.HIGH)
    GPIO.output(m2_pin, GPIO.HIGH)
    GPIO.output(m3_pin, GPIO.LOW)
  elif (step_size == 16):
    GPIO.output(m1_pin, GPIO.HIGH)
    GPIO.output(m2_pin, GPIO.HIGH)
    GPIO.output(m3_pin, GPIO.HIGH)
  else:
    print("UNSUPPORTED STEP SIZE: "+str(step_size))  

# passing in GPIO.HIGH or GPIO.LOW
def set_dir(dir):
  GPIO.output(dir_pin, dir)
  
def one_step(pulse_ms=500):

  GPIO.output(step_pin, GPIO.LOW)
  time.sleep(.001)
  GPIO.output(step_pin, GPIO.HIGH)
  time.sleep(.001)
    
def init():
  GPIO.output(step_pin, GPIO.HIGH)
  set_dir(GPIO.HIGH)
  set_step_size(1)
  GPIO.output(enable_pin, GPIO.LOW)

#######
# MAIN
#######
print("Initing")
init()
time.sleep(1)
set_step_size(16)
#set_dir(GPIO.LOW)
print("waiting")
time.sleep(1)
print("steps")
for i in range(256):
  one_step()
print("hold")
time.sleep(2)
print("done")

GPIO.output(enable_pin, GPIO.HIGH)
GPIO.cleanup()
