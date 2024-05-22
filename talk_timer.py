import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.OUT) # red
GPIO.setup(13, GPIO.OUT) # yellow
GPIO.setup(15, GPIO.OUT) # green

# set led times in units of seconds
green_time = 10*60
yellow_time = 2*60
red_time = 2*60
red_blink_time = 1*60

active = False

def button_callback(channel):
    global active
    if active == False:
        active = True
    else:
        active = False

def keep_led_on(pin, active):
    if active:
        GPIO.output(pin, GPIO.HIGH)
        sleep(1)
    else:
        GPIO.output(pin, GPIO.LOW)

def blink_led(pin, active):
    if active:
        GPIO.output(pin, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(pin, GPIO.LOW)
        sleep(0.5)
    else:
        GPIO.output(pin, GPIO.LOW)
    
def stop_led():
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)

def led_sequence():
    global active
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(15, GPIO.HIGH)
    for i in range(green_time):
        keep_led_on(15, active)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    for i in range(yellow_time):
        keep_led_on(13, active)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    for i in range(red_time):
        keep_led_on(11, active)
    for i in range(red_blink_time):
        blink_led(11, active)
    GPIO.output(11, GPIO.LOW)
    
def led_startup_sequence():
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
        sleep(0.25)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        sleep(0.25)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
        sleep(0.25)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        
led_startup_sequence()
GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback, bouncetime=500)

while True: 
    if active:
        led_sequence()
        active = False
    else:
        stop_led()


