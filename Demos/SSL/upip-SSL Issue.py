
url = 'https://files.pythonhosted.org/packages/9d/a4/afaf98be714d3701d47c47b3b6aa3d5e52bf277fe8ceb9a2e3fdb05eaf86/micropython-uasyncio-2.0.tar.gz'
proto, _, host, urlpath = url.split('/', 3)
try:
    ai = usocket.getaddrinfo(host, 443, 0, usocket.SOCK_STREAM)
except OSError as e:
    fatal("Unable to resolve %s (no Internet?)" % host, e)
#print("Address infos:", ai)
ai = ai[0]
s = usocket.socket(ai[0], ai[1], ai[2])
ussl.wrap_socket(s, server_hostname=host)


import socket,ssl
import socket
import ssl
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)#socket.IPPROTO_SEC)
ss = ssl.wrap_socket(s,server_hostname='www.google.com')
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][4])




import ssl
import socket

def https_test(host):
    addr = socket.getaddrinfo(host, 443)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect(addr)
    try:
        s = ssl.wrap_socket(s)
        s.close()
        return True
    except OSError as error:
        print("OSError: {}".format(error))
        s.close()
        return False

https_test("api.twitter.com")
https_test("files.pythonhosted.org")




package_url = 'https://files.pythonhosted.org/packages/9d/a4/afaf98be714d3701d47c47b3b6aa3d5e52bf277fe8ceb9a2e3fdb05eaf86/micropython-uasyncio-2.0.tar.gz'
package_fname = upip.op_basename(package_url)
f1 = upip2.url_open(package_url)

import usocket, ussl

url = package_url
#
global warn_ussl

if debug:
    print(url)

proto, _, host, urlpath = url.split('/', 3)
try:
    ai = usocket.getaddrinfo(host, 443, 0, usocket.SOCK_STREAM)
except OSError as e:
    fatal("Unable to resolve %s (no Internet?)" % host, e)
#print("Address infos:", ai)
ai = ai[0]

s = usocket.socket(ai[0], ai[1], ai[2])
try:
    #print("Connect address:", addr)
    s.connect(ai[-1])

    if proto == "https:":
        s = ussl.wrap_socket(s, server_hostname=host)
        if warn_ussl:
            print("Warning: %s SSL certificate is not validated" % host)
            warn_ussl = False

    # MicroPython rawsocket module supports file interface directly
    s.write("GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (urlpath, host))
    l = s.readline()
    protover, status, msg = l.split(None, 2)
    if status != b"200":
        if status == b"404" or status == b"301":
            raise NotFoundError("Package not found")
        raise ValueError(status)
    while 1:
        l = s.readline()
        if not l:
            raise ValueError("Unexpected EOF in HTTP headers")
        if l == b'\r\n':
            break
except Exception as e:
    s.close()
    raise e
