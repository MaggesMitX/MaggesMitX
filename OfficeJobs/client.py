
#!/usr/bin/env python3
# coding: utf-8


import time
import RPi.GPIO as GPIO
import Adafruit_DHT
from time import datetime
from time import sleep, strftime, time
from ast import Break

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

#Für das Relais wird 5V angeschlossen an GPIO 2, der GND an GPIO6 und 
# der Schaltimpuls an GPIO 18 (Pin12)

sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)    
#current_time = datetime.datetime.now(pytz.timezone('Germany/Berlin')) 
current_time = datetime.datetime.now().strftime('%H:%M:%S')
print("Aktuelle Zeit des Programmstartes ist", current_time)

def write_temp(temp):
    with open("/home/pi/cpu_temp.csv", "a") as log:
        temp = cpu.temperature
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
        print("Die CPU Temperatur beträgt"), temp ("Grad")
        time.sleep(60)
 
def write_time(current_time):
    if current_time == datetime.strptime("15:00:00" '%H:%M:%S') or datetime.strptime("18:30:00" '%H:%M:%S'):       #Wenn Tageszeit=15Uhr oder 18Uhr, Pin Output soll 1 werden
        GPIO.output(18, GPIO.HIGH)
        print("Job gestartet um", current_time)
        time.sleep(60)
        GPIO.output(18, GPIO.LOW)
        print("Job beendet um", current_time)
    else:
        GPIO.output(18, GPIO.LOW),
        time.sleep(0.5)              
        GPIO.cleanup(), 

def read_temp(temperature):  # vorher git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    if humidity is not None and temperature is not None:
        print('Temperatur={0:0.1f}*C  Luftfeuchtigkeit={1:0.1f}%'.format(temperature, humidity))

    elif humidity and temperature is None:
        print('Fehler beim empfangen der Daten. Bitte versuche es erneut!')
        time.sleep(10)
## Default raspivid -o - -t 0 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264