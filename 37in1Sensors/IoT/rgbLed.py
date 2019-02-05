import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

rgb = [2,3,4]
for pin in rgb:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,1)

try:
    while True:
        request = input("RGB:")
        if(len(request)==3):
            for x in range(3):
                if(int(request[x])==1):
                    GPIO.output(rgb[x],0)
                else:
                    GPIO.output(rgb[x],1)
finally:
    GPIO.cleanup()
                    
                   
