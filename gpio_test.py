import RPi.GPIO as GPIO







def turnOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = 4
    channel2 = 3

    GPIO.setup(channel, GPIO.OUT, initial=0)
##    GPIO.setup(channel2, GPIO.OUT, initial=GPIO.HIGH)

    x=0

    while x<10111:
        x=x+1
    GPIO.output(channel, GPIO.HIGH)
  ##   GPIO.output(channel2, GPIO.HIGH)


def turnOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = 4
    channel2 = 3

    GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
   ##  GPIO.setup(channel2, GPIO.OUT, initial=GPIO.HIGH)

    x=0

    while x<10020:
        x=x+1
    GPIO.output(channel, 0)
  ##   GPIO.output(channel2, GPIO.LOW)

