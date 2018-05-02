
#callback function 
import network,machine
import time

def conncb(task):
    print("[{}] Connected".format(task))

def disconncb(task):
    print("[{}] Disconnected".format(task))


def patience(client):
    while client.status()[1] in[ 'Disconnected','Stopping']:
        time.sleep_ms(50)                        


thingspeakUrl = b"mqtt.thingspeak.com" 
thingspeakUserId = b"jos"          # EDIT - enter Thingspeak User ID
thingspeakMqttApiKey = "U31KDACARRXDWGSF" # EDIT - enter Thingspeak MQTT API Key (Needs to be generated)
machine.loglevel('*', machine.LOG_DEBUG)
machine.loglevel('[Mqtt client]', machine.LOG_DEBUG)




#test to broker that does NOT allow lwt
#Do not set CleanSession flag to 0. 
client = network.mqtt(  'client_10713646',
                        "mqtt.thingspeak.com",
                        user='jos',
                        password=thingspeakMqttApiKey,
                        cleansession=True)
patience(client)
print(client)

client.stop()
patience(client)
client.free()

#default LWT = none 
client = network.mqtt(  'client_10713646',
                        "mqtt.thingspeak.com",
                        user='jos',
                        password=thingspeakMqttApiKey,
                        cleansession=True)
patience(client)
client

client.stop()
patience(client)
client.free()

#test to broker that does support lwt
client = network.mqtt(  'client_10713646',
                        "test.mosquitto.org",
                        cleansession=True,
                        lwt_topic="/jos",
                        lwt_message="offline",
                        retain=True,keepalive=10)
patience(client)
client.publish("/jos",'online')
client


#test to broker that does support lwt
client = network.mqtt(  'MCUName',
                        "test.mosquitto.org",
                        clientid='client_10713646',
                        cleansession=True,
                        lwt_topic="/jos",
                        lwt_message="offline",
                        retain=True,keepalive=10)


#test to broker that does support lwt
client = network.mqtt(  'Task1',
                        "test.mosquitto.org",
                        clientid='client_10713646',
                        cleansession=True,
                        lwt_topic="/jos",
                        lwt_message="offline",
                        retain=True,keepalive=10,
                        secure=True)
                        

#test to broker that does support lwt
client2 = network.mqtt(  'Task2',
                        "test.mosquitto.org",
                        clientid='client_10713642',
                        cleansession=True,
                        lwt_topic="/jos",
                        lwt_message="offline-too",
                        retain=True,keepalive=10,
                        secure=True)
client2.publish("/jos",'online-too')                        
