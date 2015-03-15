#!/usr/bin/env python
from MCP3008 import *
from Setup import *
import RPi.GPIO as GPIO

DEBUG = 0

# IR proximity sensor connected to adc #0
sensor_adc = 0
#-------------- THE FUN STARTS HERE! ---------------


# read the analog pin (the sensor reading)
proximity = readadc(sensor_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)



# sleep for half a second
time.sleep(0.5)
