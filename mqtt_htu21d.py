#!/usr/bin/env python
import time
import paho.mqtt.client as mqtt
from sensor.HTU21D import HTU21D

#host = ""
#port = 
#queue =
#interval = 
#clientID = ""



## I2C bus=1, Address=0x40
#htu = HTU21D(1, 0x40)

#h = htu.humidity()  # read humidity
##print(h)            # namedtuple
##print(h.RH)         # relative humidity

#t = htu.temperature()  # read temperature
##print(t)               # namedtuple
##print(t.F)             # Fahrenheit

##h, t = htu.all()  # read both at once'



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("192.168.178.202", 1883, 60)

client.loop_start()
hOld = 0
tOld = 0
while True:
    
    time.sleep(20)
    # I2C bus=1, Address=0x40
    htu = HTU21D(1, 0x40)

    h = htu.humidity()  # read humidity
    #print(h)            # namedtuple
    #print(h.RH)         # relative humidity
    t = htu.temperature()  # read temperature
    #print(t)               # namedtuple
    #print(t.F)             # Fahrenheit
    if hOld == h :
        continue
    else:
           #h, t = htu.all()  # read both at once
        client.publish("home/cellarleft/humidity", "pitwo, " + str(round(h.RH,1) )  )
        #client.publish("home/cellarleft/temperature", "pitwo, " + str(round(t.C ,1)) )

    hOld = h
    

    if tOld == t :
        continue
    else:
           #h, t = htu.all()  # read both at once
        #client.publish("home/cellarleft/humidity", "pitwo, " + str(round(h.RH,1) )  )
        client.publish("home/cellarleft/temperature", "pitwo, " + str(round(t.C ,1)) )

    tOld = t

   # time.sleep(10)
    #client.publish("home/cellarleft/humidityview",  str(round(h.RH,2) ))
   # client.publish("home/cellarleft/temperatureview",  str(round(t.C ,2) ))
