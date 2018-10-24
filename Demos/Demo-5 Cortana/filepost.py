"""try: 
    import urllib.urequest
except:
    import upip
    upip.install('micropython-urllib')
    #upip.install('micropython-urllib.parse')
    upip.install('micropython-urllib.urequest')
    #import urllib
    import urllib.urequest


"""

import ujson
import usocket

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

    ai = usocket.getaddrinfo(host, port, 0, usocket.SOCK_STREAM)
    ai = ai[0]

    s = usocket.socket(ai[0], ai[1], ai[2])
    try:
        s.connect(ai[-1])
        if proto == "https:":
            s = ussl.wrap_socket(s, server_hostname=host)

        s.write(method)
        s.write(b" /")
        s.write(path)
        s.write(b" HTTP/1.0\r\nHost: ")
        s.write(host)
        s.write(b"\r\n")

        if data:
            s.write(b"Content-Length: ")
            s.write(str(len(data)))
            s.write(b"\r\n")
        elif datafile:
            s.write(b"Ocp-Apim-Subscription-Key: 0366c4649003438ea99891d9006809bd\r\n") 
            s.write(b"Content-Type: application/octet-stream\r\n") 
            s.write(b"cache-control: no-cache\r\n") 
            s.write(b"Content-Length: ")
            s.write(str( 3806))             #todo: lookup length of file 
            s.write(b"\r\n")
            s.write(b"Connection: close\r\n") 
        s.write(b"\r\n")
        if data:
            s.write(data)
        elif datafile:
            with open(datafile,'rb') as f:
                while True:
                    data = f.read(512)  
                    if not data:
                        break
                    print('write')
                    s.write(data)

        l = s.readline()
        l = l.split(None, 2)
        print(l)
        status = int(l[1])
        while True:
            l = s.readline()
            if not l or l == b"\r\n":
                break
            #print(l)
            if l.startswith(b"Transfer-Encoding:"):
                if b"chunked" in l:
                    raise ValueError("Unsupported " + l)
            elif l.startswith(b"Location:"):
                raise NotImplementedError("Redirects not yet supported")
    except OSError:
        s.close()
        raise

    return s

import gc;gc.collect()

fname = 'foto/Jos.jpg'
url = 'https://httpbin.org/post'
url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true'
url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
try:
    socket = urlopen(url, method='POST',datafile='foto/Jos.jpg')
    resp = socket.readline()

except:
    print("An Error while calling Face detection")

finally:
    socket.close()

faces = ujson.loads(resp)

for face in faces:
    print ("a {} year old {}".format( face['faceAttributes']['age'], face['faceAttributes']['gender']) )


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



