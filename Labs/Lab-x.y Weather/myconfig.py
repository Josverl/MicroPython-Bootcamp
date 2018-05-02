"Retrieve or set the configuration used"
from machine import nvs_getstr,nvs_setstr,loglevel,LOG_NONE
#
loglevel('nvs',LOG_NONE)
wifi_ssid = nvs_getstr('SSID')
if not wifi_ssid:
    wifi_ssid=b'IOTBOOTCAMP'

wifi_psk = nvs_getstr('PSK')
if not wifi_psk:
    wifi_psk = 'MicroPython'
   
'''
Use the below commands to store an override in NVRAM 

from machine import nvs_getstr,nvs_setstr
nvs_setstr('SSID',b'MyWiFi')
nvs_setstr('PSK',b'WiFi-Password')

''' 
