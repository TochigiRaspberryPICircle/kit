#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

INTAVAL = 600
SLEEPTIME = 5

SENSOR_PIN = 9
LED_PIN = 2

GPIO.cleanup()

GPIO.setmode( GPIO.BCM )
GPIO.setup( SENSOR_PIN, GPIO.IN )
GPIO.setup( LED_PIN, GPIO.OUT)

st = time.time() - INTAVAL

while True:
    if ( GPIO.input(SENSOR_PIN) == GPIO.HIGH ) and (st + INTAVAL < time.time() ):
        st = time.time()
        GPIO.output(LED_PIN, GPIO.HIGH) # True
        print("true")
    else:
    	GPIO.output(LED_PIN, GPIO.LOW) # False
    	print("false")
    
    time.sleep( SLEEPTIME )

