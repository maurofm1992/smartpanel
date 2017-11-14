import RPi.GPIO as GPIO







def turnOn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = pin

    GPIO.setup(channel, GPIO.OUT)



    GPIO.output(channel, GPIO.HIGH)


def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = pin

    GPIO.setup(channel, GPIO.OUT)



    GPIO.output(channel, 0)
