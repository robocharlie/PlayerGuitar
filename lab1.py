
import RPi.GPIO as gpio
import time

jumper1 = 27
jumper2 = 24

led1 = 4
led2 = 17

gpio.setmode(gpio.BCM)
gpio.setup(jumper1, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(jumper2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)

def myCallback(channel):
        if channel == 27:
                gpio.output(led1, 1)
                time.sleep(1)
                gpio.output(led1, 0)
        else:
                gpio.output(led2, 1)
                time.sleep(1)
                gpio.output(led2, 0)
gpio.add_event_detect(
        jumper1, gpio.RISING,
        callback=myCallback, bouncetime=100)
gpio.add_event_detect(
        jumper2, gpio.RISING,
        callback=myCallback, bouncetime=100)

try:
        while True:
                pass
except:
        gpio.cleanup()
