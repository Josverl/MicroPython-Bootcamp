import ujson
import usocket
import logging
import gc
import uos as os

#Logging 
log = logging.getLogger("POST")
log.setLevel(logging.ERROR)
#only during debug 
#log.setLevel(logging.DEBUG)

#Utility 
def internet_connected():
    "test actual internet connectivity"
    try:
        socket = urlopenbin(b'http://www.msftncsi.com/ncsi.txt')
        resp = socket.readline()
    finally:
        if socket :
            socket.close()
    return (resp == b'Microsoft NCSI')
    
def filesize(fname):
    try:
        s = os.stat(fname)[6]
    except:
        s = 0 
    return s

#derived from urllib.urequests  module 
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
        #HTTP Start 
        s.write(b"{} /{} HTTP/1.0\r\n".format(method,path))
        #Headers todo: Pass in headers  
        s.write(b"Ocp-Apim-Subscription-Key: 0366c4649003438ea99891d9006809bd\r\n")
        s.write(b"Accept: application/json\r\n")
        s.write(b"Host: {}:{}\r\n".format(host,port))

        if data:
            log.debug('Send Data')
            s.write(b"Content-Length: ")
            s.write(str(len(data)))
            s.write(b"\r\n")
        elif datafile:
            log.debug('Send binary Data File')
            s.write(b"Content-Type: application/octet-stream\r\n")
            s.write(b"cache-control: no-cache\r\n")
            s.write(b"content-length: {}\r\n".format(str(filesize(datafile)) ))
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
        log.debug('---sent->>')
        l = s.readline()
        log.debug('<<-hdrs--')
        log.info(l)
        log.debug('==')
        
        #Read the first status returned.
        l = l.split(None, 2)
        log.debug(l)
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

def detect_faces_binary (fname = None):
    url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    #url = 'http://192.168.137.1:8888/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    s2 = urlopen(url, method='POST',datafile=fname)
    log.debug("Returned")
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
    try:
        log.info(resp_body)            
        faces = ujson.loads(resp_body)
        #print(response)
    except :
        raise RuntimeError("Problem communicating with Cortana.")
    return faces

def process_faces(faces):
    for face in faces:
        print ("I see a {} year old {}".format( 
            face['faceAttributes']['age'], 
            face['faceAttributes']['gender']
        ), end=' ')
        #print( face['faceId'] )
        #print( face['faceAttributes'] )
        #print( face['faceAttributes']['gender'] )
        #print( face['faceAttributes']['age'] )

        print( "with {} hair, {} and {}".format(
            face['faceAttributes']['hair']['hairColor'][0]['color'],  #main haircolor
            ", ".join( face['faceAttributes']['facialHair'] ),
            face['faceAttributes']['glasses'] 
        )) 
        emotion = face['faceAttributes']['emotion']
        print ( sorted(emotion, key=emotion.__getitem__)[:1] )
        # In order of sorted values: [1, 2, 3, 4]


#Demo from /flash/foto
if True:
    for fname in os.listdir('/flash/foto'):
        print('---------------------------------------------------------------')        
        print( "Foto : /flash/foto/{}".format(fname) )
        faces = detect_faces_binary( "/flash/foto/{}".format(fname))
        process_faces(faces)
        print('---------------------------------------------------------------')

#demo from /sd/foto
if False:
    os.sdconfig(os.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
    os.mountsd()
    for fname in os.listdir('/sd/foto2'):
        print('---------------------------------------------------------------')
        print( "Foto : /sd/foto/{}".format(fname) )
        faces = detect_faces_binary( "/sd/foto/{}".format(fname) )
        process_faces(faces)
        print('---------------------------------------------------------------')