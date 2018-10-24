#LoBo urequests modules


import requests

requests.debug(True)
url = 'https://httpbin.org/post'
fname = '/flash/foto/Jos.jpg'
#f =  open( fname, 'rb')
#f.close()
p_simple = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false'
}

p={'a':'b'}
# post('URL',post[String/Dict])
# postdata cannot be an empty dict 
r = requests.post(url,"")
print (r.__class__)
r[2]

r = requests.post(url,p_simple,file=fname)
print (r.__class__)
r
[2]


r2 = requests.post(url=purl,file=fname)

#https://stackoverflow.com/questions/68477/send-file-using-post-from-a-python-script
#The only thing that stops you from using urlopen directly on a file object is the fact that the builtin file object lacks a len definition. A simple way is to create a subclass, which provides urlopen with the correct file. I have also modified the Content-Type header in the file below.
import os
import urllib2

boo=bar 

x=open()

import uio 
class DataFile(uio.FileIO):
    def __init__(self, *args, **keyws):
        #uio.FileIO.__init__(self, *args, **keyws)
        uio.open( *args, **keyws)
    def __len__(self):
        #todo: adapt for micropython
        #return int(os.fstat(self.fileno())[6])
        return int(3806)

theFile = DataFile('foto/Jos.jpg', 'rb')

theUrl = "http://example.com/abcde"
theHeaders= {'Content-Type': 'text/xml'}

theRequest = urllib2.Request(theUrl, theFile, theHeaders)

response = urllib2.urlopen(theRequest)

theFile.close()


for line in response:
    print line