# the curl library is a simple way to access web servers on the internet 
# https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/curl
import curl

#get a file from a webserver http://loboris.eu/ESP32/info.txt
response = curl.get('loboris.eu/ESP32/info.txt')
if response:
    #response[0]                #return code 
    #print(response[1])         #headers
    print(response[2])          #body

