#!/usr/bin/python
# coding=utf-8
 
# Needed modules will be imported
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import tweepy
import smtplib
#from twython import Twython  
#import json
 
# The break of 2 seconds will be configured here
sleeptime = 2
 
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHTSensor = Adafruit_DHT.DHT11
 
# The pin which is connected with the sensor will be declared here
GPIO_Pin = 2
 
print('KY-015 sensortest - temperature and humidity')

#with open("twitter_credentials.json", "r") as file:  
#    creds = json.load(file)

#python_tweets = Twython('XXXX', 'XXXX')
# personal details 
consumer_key ="XXXX"
consumer_secret ="XXXX"
access_token ="XXXX"
access_token_secret ="XXXX"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)

#api.update_status(status ='temperature = {0:0.1f}°C  | rel. humidity = {1:0.1f}%'.format(temper, humid))

#Gmail
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("bhgtankita@gmail.com", "Sunstar$*123456") 
  
# message to be sent 
message = "temperature = {0:0.1f}C  | rel. humidity = {1:0.1f}%".format(temper, humid)
  
# sending the mail 
s.sendmail("bhgtankita@gmail.com", "gautham.k.28@gmail.com", message) 
  
# terminating the session 
s.quit() 

try:
    while(1):
        # Measurement will be started and the result will be written into the variables
        humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
 
        print("-----------------------------------------------------------------")
        if humid is not None and temper is not None:
 
            # The result will be shown at the console
            print('temperature = {0:0.1f}°C  | rel. humidity = {1:0.1f}%'.format(temper, humid))
         
        # Because of the linux OS, the Raspberry Pi has problems with realtime measurements.
        # It is possible that, because of timing problems, the communication fails.
        # In that case, an error message will be displayed - the result should be shown at the next try.
        else:
            print('Error while reading - please wait for the next try!')
        print("-----------------------------------------------------------------")
        print("")
        time.sleep(sleeptime)
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
    GPIO.cleanup()
