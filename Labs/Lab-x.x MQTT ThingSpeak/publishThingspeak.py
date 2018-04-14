# The MIT License (MIT)
# Copyright (c) 2017 Mike Teachman
# https://opensource.org/licenses/MIT
# 
# Publish data to a Thingspeak channel using the MQTT protocol
#
# Micropython implementation using the ESP8266 platform
# Tested using Micropython v1.9.3 (Nov 1, 2017)
#
# Tested using Hardware:
# - Adafruit Feather HUZZAH ESP8266 
#
# prerequisites:
# - Thingspeak account
# - Thingspeak channel to publish data
# - Thinkspeak Write API Key for the channel
# - Thinkspeak MQTT API Key for the account
#
 
import network,sys
if sys.platform != 'esp32_LoBo': 
    from umqtt.robust import MQTTClient
import utime
import uos
import gc

  
#
# create a random MQTT clientID 
#
randomNum = int.from_bytes(uos.urandom(3), 'little')
myMqttClient = bytes("client_"+str(randomNum), 'utf-8')

#generate clientID based on the mac address 
import machine, binascii
myMqttClient = b"client_" + binascii.hexlify(machine.unique_id())
myMqttClient = "1234"

#
# connect to Thingspeak MQTT broker
# connection uses unsecure TCP (port 1883)
# 
# Steps to change to a secure connection (encrypted) using TLS
#   a) change port below to "port=8883
#   b) add parameter "ssl=True"
#   NOTE:  TLS uses about 9k bytes of the heap. That is a lot.
#          (about 1/4 of the micropython heap on the ESP8266 platform)
#
thingspeakUrl = "mqtt.thingspeak.com" 
thingspeakUserId = "josverlinde"          # EDIT - enter Thingspeak User ID
thingspeakMqttApiKey = "ZWH8LQHCU7L9ETXA" # EDIT - enter Thingspeak MQTT API Key (Needs to be generated)
machine.loglevel('[Mqtt client]', machine.LOG_DEBUG)
client = network.mqtt(myMqttClient,          #clientID
                    thingspeakUrl,       #server
                    user=thingspeakUserId,      #user
                    password=thingspeakMqttApiKey)
                        
if sys.platform == 'esp32_LoBo': 
    machine.loglevel('[Mqtt client]', machine.LOG_DEBUG)
    client = network.mqtt(myMqttClient,          #clientID
                        thingspeakUrl,       #server
                        user=thingspeakUserId,      #user
                        password=thingspeakMqttApiKey)
#                        , cleansession=True)
    #                    connected_cb=conncb, 
    #                    disconnected_cb=disconncb, 
    #                    subscribed_cb=subscb, 
    #                    published_cb=pubcb, 
    #                    data_cb=datacb)
    client.start()
else:
    client = MQTTClient(client_id=myMqttClient, 
                        server=thingspeakUrl, 
                        user=thingspeakUserId, 
                        password=thingspeakMqttApiKey, 
                        port=1883)
    client.connect()

#
# publish free heap to Thingspeak using MQTT
#
utime.sleep(5)

thingspeakChannelId = "470467"                 # EDIT - enter Thingspeak Channel ID
thingspeakChannelWriteApiKey = "QTR27E88RNG8QXC0" # EDIT - enter Thingspeak Write API Key
publishPeriodInSec = 5 
#while True:
    
freeHeapInBytes = gc.mem_free()
credentials = bytes("channels/{:s}/publish/{:s}".format(thingspeakChannelId, thingspeakChannelWriteApiKey), 'utf-8')  
payload = bytes("field1={:.1f}\n".format(freeHeapInBytes), 'utf-8')
client.publish(credentials, payload)

#utime.sleep(publishPeriodInSec)
  
#client.disconnect()  

