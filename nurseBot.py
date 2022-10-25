#!/usr/bin/python
# Import necessary libraries for communication and display use


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




try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
light_channel = AnalogIn(mcp, MCP.P2)
sound_channel = AnalogIn(mcp, MCP.P5)


sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
degrees_c = sensor.data.temperature
humidity = sensor.data.humidity
gas = sensor.data.gas_resistance
max_raw_light_num = 7500
light = interp(int(light_channel.value),[0,max_raw_light_num],[0,100]) 


#print('\n\nTemprature: '+ str(degrees_c))


apiKey="hYn5IyqJh7U9lfVdiSvSyJb1"
secretKey="ExMVG1hBAbrE0MFpyEwJJGJXAlT6zYwr"
bbt = BBT(apiKey, secretKey)


bpm_resource = Resource(bbt,"NursingBot","heartbeat")
temperature_resource = Resource(bbt,"NursingBot","temperature")
humidity_resource = Resource(bbt,"NursingBot","humidity")
gas_resource = Resource(bbt,"NursingBot","gas")
sound_resource = Resource(bbt,"NursingBot","sound")
light_resource = Resource(bbt,"NursingBot","light")

bpm = 0

p = Pulsesensor()
p.startAsyncBPM()


def startHeartbeatSensor():
    try:
            bpm = p.BPM
            if bpm > 0:
                print("BPM: %d" % bpm)
                
                display.lcd_display_string("Heartbeat",1)
                display.lcd_display_string(str(bpm), 2)
                bpm_resource.write(bpm)
                
            else:
                print(bpm)
                time.sleep(1)
    except:
        p.stopAsyncBPM()


def startBme680():
        temperature_resource.write(degrees_c)
        gas_resource.write(gas)
        humidity_resource.write(humidity)
        #light is not part of bme680 but its nice to ahave all this data sending at the same time
        light_resource.write(light)
    


def callback(channel):
        if GPIO.input(channel):
                print("Sound Detected!")
                display.lcd_display_string("Sound Detected",1)
                sound_resource.write("Sound detected")

        else:
                print ("No sound detected")
                display.lcd_display_string("No sound detected",1)
                sound_resource.write("No sound detected")
        
                

def soundDetection():
   
        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
        
        GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
        


def run():
    global degrees_c
    global humidity
    startHeartbeatSensor()
    display.lcd_clear()
    display.lcd_display_string("Heartbeat",1)
    display.lcd_display_string(str(bpm), 2)
    time.sleep(5)
    startBme680()
    display.lcd_display_string("Temp: " + str(degrees_c),1)
    display.lcd_display_string("Humidity: "+ str(humidity), 2)
    time.sleep(5)
    display.lcd_clear()
    soundDetection()
    time.sleep(5)
    run()
run()

