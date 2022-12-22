
from math import degrees
import drivers
display = drivers.Lcd()

import RPi.GPIO as GPIO
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


sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
degrees_c = sensor.data.temperature
humidity = sensor.data.humidity
gas = sensor.data.gas_resistance


apiKey="hYn5IyqJh7U9lfVdiSvSyJb1"
secretKey="ExMVG1hBAbrE0MFpyEwJJGJXAlT6zYwr"
bbt = BBT(apiKey, secretKey)


temperature_resource = Resource(bbt,"NursingBot","temperature")
humidity_resource = Resource(bbt,"NursingBot","humidity")
gas_resource = Resource(bbt,"NursingBot","gas")
sound_resource = Resource(bbt,"NursingBot","sound")
light_resource = Resource(bbt,"NursingBot","light")

def startBme680():
        print(degrees_c)
        temperature_resource.write(degrees_c)
        gas_resource.write(gas)
        humidity_resource.write(humidity)
        #light is not part of bme680 but its nice to ahave all this data sending at the same time
        #light_resource.write(light)
    

def run():
    while True:
        startBme680()
        display.lcd_display_string("Temp: " + str(degrees_c),1)
        display.lcd_display_string("Humidity: "+ str(humidity), 2)
        time.sleep(5)
        display.lcd_clear()
        time.sleep(5)

run()
