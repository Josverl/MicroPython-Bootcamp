import ujson
import usocket
import logging
import gc

log = logging.getLogger("POST")

log.setLevel(logging.ERROR)
#only during debug 
log.setLevel(logging.DEBUG)

def urlopen(url, data=None, method="GET", datafile=None):
    if data is not None and method == "GET":
        method = "POST"
    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        import ussl
        port = 443
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    ai = usocket.getaddrinfo(host, port , 0, usocket.SOCK_STREAM)
    if ai==[] :
        print('Error: No internet connectivity')
        return None
    log.debug(ai)
    ai = ai[0]

    s = usocket.socket(ai[0], ai[1], ai[2])
    try:
        log.debug('Connecting')
        s.connect(ai[-1])
        if proto == "https:":
            log.debug('Wrap SSL')
            s = ussl.wrap_socket(s, server_hostname=host)
        #Just a copy
        #s.write(b"{} /{} HTTP/1.0\r\n".format(method,path))
        s.write(b"POST https://westeurope.api.cognitive.microsoft.com:443/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise HTTP/1.1\r\n")
        s.write(b"Ocp-Apim-Subscription-Key: 0366c4649003438ea99891d9006809bd\r\n")
        s.write(b"Content-Type: application/octet-stream\r\n")
        s.write(b"cache-control: no-cache\r\n")
        s.write(b"Postman-Token: cb0d1225-c1c8-43c9-8711-594c43efad08\r\n")
        s.write(b"User-Agent: PostmanRuntime/7.3.0\r\n")
        s.write(b"Accept: */*\r\n")
        s.write(b"Host: westeurope.api.cognitive.microsoft.com:443\r\n")
        s.write(b"accept-encoding: gzip, deflate\r\n")
        

        if data:
            log.debug('Send Data')
            s.write(b"Content-Length: ")
            s.write(str(len(data)))
            s.write(b"\r\n")
        elif datafile:
            log.debug('Send binary Data File')
            
            s.write(b"content-length: ")
            s.write(str( 3806))             #todo: lookup length of file 
            s.write(b"\r\n")
            s.write(b"Connection: keep-alive\r\n") 

        s.write(b"\r\n")
        if data:
            s.write(data)
        elif datafile:
            with open(datafile,'rb') as f:
                while True:
                    data = f.read(512)  
                    if not data:
                        break
                    log.debug('write')
                    s.write(data)
        log.debug('------->>')
        l = s.readline()
        log.debug('<<-------')
        log.info(l)
        log.debug('==')
        
        #Read the first status returned.
        l = l.split(None, 2)
        print(l)
        status = int(l[1])
        #read through returned headers 
        while True:
            l = s.readline()
            if not l or l == b"\r\n":
                break
            log.debug(l)
            if l.startswith(b"Transfer-Encoding:"):
                if b"chunked" in l:
                    raise ValueError("Unsupported " + l)
            elif l.startswith(b"Location:"):
                raise NotImplementedError("Redirects not yet supported")
    except OSError:
        log.debug("Error, closing socket")
        s.close()
        raise
    s.setblocking(False)
    return s

import gc;gc.collect()

#url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true'
url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'

fiddler = 'http://192.168.137.1:8888/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'

fname = '/flash/foto/Jos.jpg'
s2 = urlopen(url, method='POST',datafile=fname)
print("Returned")
#Now read the response string 
#Readline does not work :-( 
resp_body=b""
while True:
    block = s2.read(512)
    if block:
        log.debug( 'recieving body..')
        resp_body+=block
    else:
        log.debug( 'done')
        break
s2.close()
gc.collect() #Free memory

#process the return 
faces = ujson.loads(resp_body)
for face in faces:
    print ("a {} year old {}".format( face['faceAttributes']['age'], face['faceAttributes']['gender']) )

"""
print( faces[0]['faceId'] )
print( faces[0]['faceAttributes'] )
print( faces[0]['faceAttributes']['gender'] )
print( faces[0]['faceAttributes']['age'] )

print( faces[0]['faceAttributes']['hair']['hairColor'][0]['color']  ) #main haircolor
print( faces[0]['faceAttributes']['glasses'] )

print( faces[0]['faceAttributes']['facialHair'] )
print( faces[0]['faceAttributes']['emotion'] )

emotion = faces[0]['faceAttributes']['emotion']
print ( sorted(emotion, key=emotion.__getitem__) )
# In order of sorted values: [1, 2, 3, 4]

"""

