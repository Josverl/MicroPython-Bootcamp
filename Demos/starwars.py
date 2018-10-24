#The first thing to do is make sure we have the socket module available:
import socket

#Then get the IP address of the server:
addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)

#The getaddrinfo function actually returns a list of addresses, and each address has more information than we need. We want to get just the first valid address, and then just the IP address and port of the server. To do this use:
addr = addr_info[0][-1]
#If you type addr_info and addr at the prompt you will see exactly what information they hold.
#Using the IP address we can make a socket and connect to the server:
s = socket.socket()
s.connect(addr)

#Now that we are connected we can download and display the data:
while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')

#When this loop executes it should start showing the animation (use ctrl-C to interrupt it).