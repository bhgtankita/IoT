import RPi.GPIO as GPIO
import time
from gpiozero import Buzzer

GPIO.setmode(GPIO.BCM)

channel1 = 2
Buzzer = 11
 
CL = [0, 131, 147, 165, 175, 196, 211, 248]     # Frequency of Low C notes
 
CM = [0, 262, 294, 330, 350, 393, 441, 495]     # Frequency of Middle C notes
 
CH = [0, 525, 589, 661, 700, 786, 882, 990]     # Frequency of High C notes
 
song_1 = [  CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Notes of song1
            CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
            CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
            CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5] ]

beat_1 = [  1, 1, 3, 1, 1, 3, 1, 1,             # Beats of song 1, 1 means 1/8 beats
            1, 1, 1, 1, 1, 1, 3, 1,
            1, 3, 1, 1, 1, 1, 1, 1,
            1, 2, 1, 1, 1, 1, 1, 1,
            1, 1, 3 ]

GPIO.setup(channel1, GPIO.IN)
#GPIO.setup(channel2, GPIO.OUT)

def setup():
    GPIO.setmode(GPIO.BCM)        # Numbers GPIOs by physical location
    GPIO.setup(Buzzer, GPIO.OUT)    # Set pins' mode is output
    global Buzz                     # Assign a global variable to replace GPIO.PWM
    Buzz = GPIO.PWM(Buzzer, 440)    # 440 is initial frequency.
    Buzz.start(1)
       
def destory():
    Buzz.stop()                 # Stop the buzzer
    GPIO.output(Buzzer, 1)      # Set Buzzer pin to High
    GPIO.cleanup()           


def callback(channel1):
    print("flame detected")
    #GPIO.output(channel2, GPIO.HIGH)
    #loop()
    setup()
    
GPIO.add_event_detect(channel1, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel1, callback)

while True:
    time.sleep(1)

destory()
GPIO.cleanup()    
