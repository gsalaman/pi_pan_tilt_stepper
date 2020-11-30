import paho.mqtt.client as mqtt
import time
from datetime import datetime
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


# Callback for message
def on_message(client, userdata, message):

  print("message received: ", str(message.payload.decode("utf-8")))
  print("message topic=", message.topic)
  print("message qos=", message.qos)
  print("message retain flag=", message.retain)

######################################################
# StepperMotion object
#   data:  
#     stepper_drv: a kit.stepper object used for driver functions
#     moving:  True or False...are we in the process of taking steps?
#     dir:  either stepper.FORWARD or stepper.BACKWARD
#     current_step: which step are we currently on
#     max_steps: how many total steps do we need to take
#     step_size:  SINGLE, DOUBLE, INTERLEAVED, or MICROSTEP
#     step_delay:  ms between steps
#     last_step_time: datetime of last step 
######################################################
class StepperMotion():
  def __init__(self,stepper_drv):
    self.stepper_drv = stepper_drv
    self.moving = False
    self.dir = stepper.FORWARD 
    self.current_step = 0
    self.max_steps = 0
    self.step_size = stepper.SINGLE 
    self.step_delay = 0
    self.last_step_time = datetime.now()
    
  def stop(self):
    # don't take another step.
    self.max_steps = 0
    self.moving = False 
    self.last_step_time =  datetime.now()

  def check_for_step(self):
    if (self.moving):
      if (self.current_step < self.max_steps):
        current_time = datetime.now()
        deltaT = current_time - self.last_step_time
        if (deltaT.total_seconds() >= self.step_delay / 1000):
          # it's time to take a step.
          self.stepper_drv.onestep(direction = self.dir,
                                   style=self.step_size);

          # update vars for next time around
          self.current_step = self.current_step + 1
          self.last_step_time = current_time
      
          # if we've hit the end of our motion, stop.
          if (self.current_step >= self.max_steps):
            self.moving = "False"

      else:
        # we shouldn't get in here...we were moving, but didn't have
        # any steps left to take.  I'm gonna flag the error, clean up, 
        # and move on.
        print("Stepper driver moving with no more steps!")
        stepper.moving = False

    def set_direction(self, dir):
      self.dir = dir
  
    def set_step_size(self, step_size):
      self.step_size = step_size

    def set_step_delay(self, delay):
      self.step_delay = delay
 
    def start(self,num_steps=1):
      self.last_step_time = datetime.now()
      self.max_steps = num_steps
      self.current_step = 0
      # note that this doesn't actually START the motion; it just lets our 
      # driver function do the proper step if the time is right. 
      self.moving = True
 
    def release(self):
      self.stop()
      self.stepper_drv.release()

######################################################
# Main
######################################################

broker_address="10.0.0.46"
client = mqtt.Client("pts1_client")
client.on_message=on_message
client.connect(broker_address)
client.subscribe("pts1/#")
client.loop_start()


try:
  
  print("Pan-tilt stepper driver")
  print("ctrl-c to exit")

  kit = MotorKit()
  pan_stepper = StepperMotion(kit.stepper1)
  
  #first test:  no motion.  Nothing below this.  :)
  
  while True:
    pan_stepper.check_for_step()

    # quick sleep to aid with multiprocessing
    time.sleep(0.0001)

except KeyboardInterrupt:
  print("Exiting...")

