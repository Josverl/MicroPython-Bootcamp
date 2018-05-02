
import ujson
import urequests
import ubinascii 
dir(userName)

newSMSurl = 'https://api.twilio.com/2010-04-01/Accounts/AC43e13670164d568d820037acf9f47028/Messages.json'
#username password

userName='AC43e13670164d568d820037acf9f47028'
userPassword='[AuthToken]'
#unicode to tobytes 
creds = str.encode(userName) + b":" + str.encode(userPassword)
#base64 encoded
creds = ubinascii.b2a_base64(creds)
Headers = {'Authorization': authInfo}

message = ""

--data-urlencode 'To=+31651446844' \
--data-urlencode 'From=+3197004880586' \
--data-urlencode 'Body=Hallo, dit is een test bericht.' \

response = urequests.post(url data = message

POST

#string to bytes
my_str = "Hello MicroPython"
#unicode string to bytes
bytes = str.encode(my_str)
# Show it is byte representation
print(type(bytes), bytes)
#BYTES TO UNICODE STRING
my_decoded_str = bytes.decode(bytes)
# ensure it is string representation
print(type(my_decoded_str) ,my_decoded_str)
