import RPi.GPIO as GPIO
import time
import sys
import ta7291

if __name__ == "__main__":
  d = ta7291.ta7291(18, 24, 25)
  for power in range(0, 100, 10):
    d.drive(power)
    time.sleep(0.3)

  for power in range(100, 0, -10):
	  d.drive(power)
	  time.sleep(0.3)

  d.drive(0)
  time.sleep(3)

  d.drive(100)
  time.sleep(3)

  d.drive(0)
  time.sleep(3)

  d.drive(100)
  time.sleep(3)

  d.brake()
  time.sleep(3)

  d.cleanup()
