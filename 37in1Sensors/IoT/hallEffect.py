import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)

while True:
    if GPIO.input(2) == 0:
        print("Open")
    else:
         print("Close")

GPIO.cleanup()         
