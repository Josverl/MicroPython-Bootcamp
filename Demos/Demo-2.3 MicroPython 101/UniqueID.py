#--------------------
# Get Unique ID
#--------------------

from binascii import hexlify
import sys
id = 'unknown'
if sys.platform=='esp32_LoBo':
    #Lobo 
    id = hexlify(machine.unique_id()).decode('ascii')
else:
    wlan = network.WLAN(network.STA_IF)
    id = binascii.hexlify(wlan.config('mac')).decode('ascii')

print('Unique ID:', id)


