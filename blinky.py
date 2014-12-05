import RPi.GPIO as GPIO
import time

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)

setup_gpio()
for i in range(10):
    GPIO.output(5, 1)
    time.sleep(0.5)
    GPIO.output(5, 0)
    time.sleep(0.5)
    

    
    
