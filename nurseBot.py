
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from pulsesensor import Pulsesensor
import time
from beebotte import *
import logging
import bme680

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
degrees_c = sensor.data.temperature
humidity = sensor.data.humidity
gas = sensor.data.gas_resistance


print('\n\nTemprature: '+ str(degrees_c))


apiKey="hYn5IyqJh7U9lfVdiSvSyJb1"
secretKey="ExMVG1hBAbrE0MFpyEwJJGJXAlT6zYwr"
bbt = BBT(apiKey, secretKey)


bpm_resource = Resource(bbt,"NursingBot","heartbeat")
temperature_resource = Resource(bbt,"NursingBot","temperature")
humidity_resource = Resource(bbt,"NursingBot","humidity")
gas_resource = Resource(bbt,"NursingBot","gas")
sound_resource = Resource(bbt,"NursingBot","sound")





p = Pulsesensor()
p.startAsyncBPM()


def startHeartbeatSensor():
    try:
        while True:
            bpm = p.BPM
            if bpm > 0:
                print("BPM: %d" % bpm)
                bpm_resource.write(bpm)
            else:
                print(bpm)
            time.sleep(1)
    except:
        p.stopAsyncBPM()

def startBme680():
    while True:
        temperature_resource.write(degrees_c)
        gas_resource.write(gas)
        humidity_resource.write(humidity)

        print(gas)


    


def callback(channel):
        if GPIO.input(channel):
                print("Sound Detected!")
        else:
                print ("Sound Detected!")

#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

#startHeartbeatSensor()
startBme680()
#callback()
    
