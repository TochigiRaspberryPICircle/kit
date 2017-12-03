import webiopi
import os
import RPi.GPIO as GPIO

# GPIO number
LEFTFW  = 9   # Pin 21
RIGHTFW = 10  # Pin 19
LEFTBW  = 8   # Pin 24
RIGHTBW = 11  # Pin 23

@webiopi.macro
def tank( goback ):
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)

#  GPIO.setFunction( 8, GPIO.IN)
#  GPIO.setFunction( 9, GPIO.IN)
#  GPIO.setFunction(10, GPIO.IN)
#  GPIO.setFunction(11, GPIO.IN)

  for n in (8,9,10,11):
    GPIO.setup(n, GPIO.OUT)

  print( goback )
  if goback == "go":
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
  elif goback == "ON":
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
  elif goback == "right":
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
  elif goback == "left":
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
  elif goback == "backword":
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
  elif goback == "stop":
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
  elif goback == "off":
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
  elif goback == "qleft":
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
  elif goback == "qright":
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
  else:
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)

  return "OK"
