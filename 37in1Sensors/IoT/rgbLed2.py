import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)
GPIO.output(2,1)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,1)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)

try:
    while(True):
        request = input("RGB:")
        if(len(request)==3):
            GPIO.output(2,int(request[0]))
            GPIO.output(3,int(request[1]))
            GPIO.output(17,int(request[2]))

finally:
    GPIO.cleanup()
                    
                   
