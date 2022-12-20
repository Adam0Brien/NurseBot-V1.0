#!/usr/bin/python
# Import necessary libraries for communication and display use


from math import degrees
import drivers
display = drivers.Lcd()

import RPi.GPIO as GPIO
import time
from pulsesensor import Pulsesensor
import time
from beebotte import *
import logging
import bme680
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from numpy import interp


#MCP3008 Setup
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

#Photoresistor setup
max_raw_light_num = 7500
light = interp(int(light_channel.value),[0,max_raw_light_num],[0,100]) 


#Beebotte Credentials
apiKey="api-key-here"
secretKey="secret-key-here"
bbt = BBT(apiKey, secretKey)

#Beebotte Resources
bpm_resource = Resource(bbt,"NursingBot","heartbeat")
light_resource = Resource(bbt,"NursingBot","light")

bpm = 0

p = Pulsesensor()
p.startAsyncBPM()


def startHeartbeatSensor():
    try:
        while True:
            bpm = p.BPM
            if bpm > 0:
                print("BPM: %d" % bpm)
                display.lcd_display_string("Heartbeat",1)
                display.lcd_display_string(str(bpm), 2)
                bpm_resource.write(bpm)                
            else:
                print("No Heartbeat found: "+str(bpm))
            time.sleep(1)  
    except:
        p.stopAsyncBPM()

def LocalHeart():
    try:
        while True:
            bpm = p.BPM
            if bpm > 0:
                print("BPM: %d" % bpm)
            else:
                print("No Heartbeat found")
            time.sleep(1)
    except:
        p.stopAsyncBPM()
              
def run():
    startHeartbeatSensor()
    display.lcd_clear()
    display.lcd_display_string("Heartbeat",1)
    display.lcd_display_string(str(bpm), 2)
    time.sleep(5)
    light_resource.write(light) #sending light value to beebotte
 
    run()

run()
