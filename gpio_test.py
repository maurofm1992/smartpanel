import RPi.GPIO as GPIO







def turnOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = 4
    channel2 = 3

    GPIO.setup(channel, GPIO.OUT)
##    GPIO.setup(channel2, GPIO.OUT, initial=GPIO.HIGH)



    GPIO.output(channel, GPIO.HIGH)
  ##   GPIO.output(channel2, GPIO.HIGH)


def turnOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = 4
    channel2 = 3

    GPIO.setup(channel, GPIO.OUT)
   ##  GPIO.setup(channel2, GPIO.OUT, initial=GPIO.HIGH)



    GPIO.output(channel, 0)
  ##   GPIO.output(channel2, GPIO.LOW)
