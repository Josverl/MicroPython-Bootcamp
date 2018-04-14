#minimal MQTT

import network,sys,machine
import utime
import uos

import gc
machine.loglevel('[Mqtt client]', machine.LOG_DEBUG)
myMqttClient = bytes("client_123", 'utf-8')
thingspeakUrl = "mqtt.thingspeak.com" 
thingspeakUserId = "josverlinde"          # EDIT - enter Thingspeak User ID
thingspeakMqttApiKey = "ZWH8LQHCU7L9ETXA" # EDIT - enter Thingspeak MQTT API Key (Needs to be generated)
machine.loglevel('[Mqtt client]', machine.LOG_DEBUG)
client = network.mqtt(myMqttClient,          #clientID
                    thingspeakUrl,       #server
                    user=thingspeakUserId,      #user
                    password=thingspeakMqttApiKey)
