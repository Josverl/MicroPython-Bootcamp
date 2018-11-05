#----------------------
#connect to Thingspeak 
#----------------------

write('Connect to Thingspeak\n')

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

#Channel : My Weather Demo 
thingspeakChannelId = "498254"                      # EDIT - enter Thingspeak Channel ID
thingspeakChannelWriteApiKey = "FOU9KYJM6NDHH43F"   # EDIT - enter Thingspeak Write API Key




thingspeakPort = 1883
useSSL = False

client = MQTTClient(client_id=myMqttClient, 
                    server=thingspeakUrl, 
                    user=thingspeakUserId, 
                    password=thingspeakMqttApiKey, 
                    port= thingspeakPort,
                    ssl = useSSL)

status = client.connect()
tsChannel = bytes("channels/{:s}/publish/{:s}".format(thingspeakChannelId, thingspeakChannelWriteApiKey), 'utf-8')  

if status == 0:
    writeln('Connected OK')
else:    
    writeln('Error !')


####################

While 1:
    #-------------------
    #Send the data to TS
    #------------------- 
    #enable only when mqtt is enabled   
    sensordata = "field1={:.1f}&field2={:.1f}&field3={:.1f}&field4={:.1f}\n".format(
        sensor.data.temperature,
        sensor.data.pressure,
        sensor.data.humidity,
        sensor.data.gas_resistance)
    client.publish(tsChannel, bytes(sensordata, 'utf-8') ) 
