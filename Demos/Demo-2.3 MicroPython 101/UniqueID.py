#--------------------
# Get Unique ID
#--------------------
from binascii import hexlify
import machine

id = hexlify(machine.unique_id()).decode('ascii')

print('Unique ID:', id)
