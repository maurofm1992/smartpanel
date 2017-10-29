import RPi.GPIO as GPIO







def turnOn():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = 2
    channel2 = 3

    GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(channel2, GPIO.OUT, initial=GPIO.HIGH)

    state = 0
    x=0

    while x<10000:
        x=x+1
    GPIO.output(channel, GPIO.HIGH)
    GPIO.output(channel2, GPIO.HIGH)

def turnOff():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    channel = 2
    channel2 = 3

    GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(channel2, GPIO.OUT, initial=GPIO.HIGH)

    state = 0
    x=0

    while x<100000:
        x=x+1
    GPIO.output(channel, GPIO.LOW)
    GPIO.output(channel2, GPIO.LOW)

