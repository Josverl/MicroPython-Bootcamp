#Main

print('Main: ready to start doing things')

import curl
response = curl.get('loboris.eu/ESP32/info.txt')
#response[0]                #return code 
#print(response[1])         #headers
print(response[2])          #body
