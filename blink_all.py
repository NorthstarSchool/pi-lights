import RPi.GPIO as GPIO
import time

def setup_gpio():
    # This function sets up the GPIO ports
    # to control LEDs on ports 5, 6, 13, & 19
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)

def blink_led(gpio_num):
    # this function will turn the LED at port gpio_num
    # on for 0.5 seconds and off for 0.5 seconds
    GPIO.output(gpio_num, 1)
    time.sleep(0.5)
    GPIO.output(gpio_num, 0)
    time.sleep(0.5)

setup_gpio()
for led_num in [5, 6, 13, 19]:
    blink_led(led_num)
    

    
    
