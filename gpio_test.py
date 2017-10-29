import RPi.GPIO as GPIO




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
channel = 2

GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

state = 0
x=0

while x<10000:
    x=x+1
GPIO.output(channel, GPIO.HIGH)


while x<10000000:
    x=x+1
GPIO.output(channel, GPIO.LOW)
