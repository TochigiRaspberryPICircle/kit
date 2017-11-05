import RPi.GPIO as GPIO
import time
import sys

class ta7291:
  def __init__(self, pwm, in1, in2):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pwm, GPIO.OUT)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)

    self.in1 = in1
    self.in2 = in2
    self.p = GPIO.PWM(18, 50)

  def drive(self, speed):
    if speed > 0:
      GPIO.output(self.in1, 1)
      GPIO.output(self.in2, 0)
      self.p.start(speed)
    
    if speed < 0:
      GPIO.output(self.in1, 0)
      GPIO.output(self.in2, 1)
      self.p.start(-speed)

    if speed == 0:
      GPIO.output(self.in1, 0)
      GPIO.output(self.in2, 0)

  def brake(self):
    GPIO.output(self.in1, 1)
    GPIO.output(self.in2, 1)
    time.sleep(0.5)

  def cleanup(self):
    self.brake()
    GPIO.cleanup()

if __name__ == "__main__":
  pass
