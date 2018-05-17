# The MIT License (MIT)
# Copyright (c) 2017 Mike Teachman
# https://opensource.org/licenses/MIT
# 
# Publish data to a Thingspeak channel using the MQTT protocol
#
# Micropython implementation using the ESP8266 platform
# Tested using Micropython v1.9.3 (Nov 1, 2017)
#
# prerequisites:
# - Thingspeak account
# - Thinkspeak MQTT API Key for the account
# - Thingspeak channel to publish data
# - Thinkspeak Write API Key for the channel
#
 
import network,sys
from umqtt.robust import MQTTClient
import utime
import uos
import gc

#create  MQTT clientID based on the mac address 
import machine, binascii
MAC = binascii.hexlify(machine.unique_id()).decode("utf-8")
myMqttClient = "M5Stack_{}".format(MAC)

# connect to Thingspeak MQTT broker
# connection uses unsecure TCP (port 1883)
thingspeakUrl = "mqtt.thingspeak.com"

thingspeakUserId = "josverlinde"                    # EDIT - enter Thingspeak User ID
thingspeakMqttApiKey = "ZWH8LQHCU7L9ETXA"           # EDIT - enter Thingspeak MQTT API Key (Needs to be generated)

'''
Demo = 2
if Demo == 1: 
    thingspeakChannelId = "470467"                      # EDIT - enter Thingspeak Channel ID
    thingspeakChannelWriteApiKey = "QTR27E88RNG8QXC0"   # EDIT - enter Thingspeak Write API Key
else if Demo == 2: 
'''
thingspeakChannelId = "496737"                      # EDIT - enter Thingspeak Channel ID
thingspeakChannelWriteApiKey = "GOO9JT7WUEFH91EA"   # EDIT - enter Thingspeak Write API Key


# Steps to change to a secure connection (encrypted) using TLS
#   a) change port below to "port=8883
#   b) add parameter "ssl=True" 
thingspeakPort = 1883
useSSL = False

client = MQTTClient(client_id=myMqttClient, 
                    server=thingspeakUrl, 
                    user=thingspeakUserId, 
                    password=thingspeakMqttApiKey, 
                    port= thingspeakPort,
                    ssl = useSSL)

status = client.connect()
if status != 0: 
    print('Error')

#
# publish free heap to Thingspeak using MQTT
#
utime.sleep(5)

publishPeriodInSec = 5 
credentials = bytes("channels/{:s}/publish/{:s}".format(thingspeakChannelId, thingspeakChannelWriteApiKey), 'utf-8')  
print(credentials)

while True:    
    freeHeapInBytes = gc.mem_free()
    
    payload = "field1={:.1f}&field2={:.1f}\n".format(
            freeHeapInBytes,
            (machine.internal_temp())[1]
            )
    client.publish(credentials, bytes(payload, 'utf-8') ) 
    print("Logged data :{}".format(payload))
    utime.sleep(publishPeriodInSec)

 
#client.disconnect()  

