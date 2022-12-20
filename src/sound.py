#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from pulsesensor import Pulsesensor
import time
import requests


channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

IFTTT_KEY = "jnrl2wAUPhKNBs4SceVMEZ5RXeqA0jlcL8xeXQF8Dhx"

event_name = "Sound"
url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{IFTTT_KEY}"
payload = {"value1": 1}

#SOUND SENSOR SETUP
def callback(channel):
        if GPIO.input(channel):
                print("Sound Detected!")
            
                response = requests.post(url, json=payload)
                print(response.status_code)
        else:
                print ("Sound Detected!")
                response = requests.post(url, json=payload)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) 
GPIO.add_event_callback(channel, callback)  




       
