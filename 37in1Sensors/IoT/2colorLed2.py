# Needed modules will be imported and configured.
import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   
# Output pin declaration for the LEDs.
LED_Red = 2
LED_Green = 3
GPIO.setup(LED_Red, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_Green, GPIO.OUT, initial= GPIO.LOW)
   
print("LED-Test [press ctrl+c to end the test]")
 
# Main program loop
try:
        while True:
            print("LED Red will be on for 3 seconds")
            GPIO.output(LED_Red,GPIO.HIGH) #LED will be switched on
            GPIO.output(LED_Green,GPIO.LOW) #LED will be switched off
            time.sleep(3) # Waitmode for 3 seconds
            print("LED Green will be on for 3 seconds")
            GPIO.output(LED_Red,GPIO.LOW) #LED will be switched off
            GPIO.output(LED_Green,GPIO.HIGH) #LED will be switched on
            time.sleep(3) #Waitmode for another 3 seconds in which the LEDs are shifted
   
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
