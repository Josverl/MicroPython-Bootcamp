"""
IoT Bootcamp - dfplayer.py 
Marcus Tarquinio, Jos Verlinde
28th Abril 2018

Modified from original Botdemy code
http://www.instructables.com/id/MicroPython-IoT-Rover-Based-on-WeMos-D1-ESP-8266EX/
"""

import socket
import machine
import time 

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head>
<title>IoT Bootcamp - Tank Control</title>
<style>
body {background-color: black}
h1 {color:red}

button {
        color: red;
        height: 200px;
        width: 200px;
        background:black;
        border: 3px solid #4CAF50; /* Green */
        border-radius: 50%;
        font-size: 250%;
        position: center;
}
</style>
</head>
<body>
<center><h1>IoT Bootcamp - Tank Control</h1>
<form>
<div><button name="CMD" value="forward" type="submit">Forward</button></div>
<div><button name="CMD" value="left" type="submit">Left</button>
<button name="CMD" value="stop" type="submit">Stop</button>
<button name="CMD" value="right" type="submit">Right</button></div>
<div><button name="CMD" value="back" type="submit">Back</button></div>
</form>
</center>
</body>
</html>
"""

# ESP-12E Motor Shield based on ESP8266
# https://smartarduino.gitbooks.io/user-mannual-for-esp-12e-motor-shield/content/interface.html
#D1 -> GPIO5 -> PWMA(motor A - right)
#D2 -> GIOO4 -> PWMB (motor B - left)
#D3 -> GPIO0 -> DA (direction of motor A - right)
#D4 -> GPI02 -> DB (direction of motor B - left)

MotorRightPWM = machine.Pin(5, machine.Pin.OUT)
MotorLeftPWM = machine.Pin(4, machine.Pin.OUT)

MotorRightDIR = machine.Pin(0, machine.Pin.OUT)
MotorLeftDIR = machine.Pin(2, machine.Pin.OUT)

def forward():
  MotorRightPWM.value(1)
  MotorLeftPWM.value(1)
  MotorRightDIR.value(0)
  MotorLeftDIR.value(0)

def back():
  MotorRightPWM.value(1)
  MotorLeftPWM.value(1)
  MotorRightDIR.value(1)
  MotorLeftDIR.value(1)

def left():
  MotorRightPWM.value(1)
  MotorLeftPWM.value(1)
  MotorRightDIR.value(0)
  MotorLeftDIR.value(1)
  time.sleep_ms(100)
  stop()

def right():
  MotorRightPWM.value(1)
  MotorLeftPWM.value(1)
  MotorRightDIR.value(1)
  MotorLeftDIR.value(0)
  time.sleep_ms(100)
  stop()

def stop():
  MotorRightPWM.value(0)
  MotorLeftPWM.value(0)
  MotorRightDIR.value(0)
  MotorLeftDIR.value(0)
 
#Setup Socket WebServer
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()

#new?
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', 80))
s.listen(5)
print("Listening, connect your browser to http://<this_host>:80/")

counter = 0

while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)

    CMD_forward = request.find('/?CMD=forward')
    CMD_back = request.find('/?CMD=back')
    CMD_left = request.find('/?CMD=left')
    CMD_right = request.find('/?CMD=right')
    CMD_stop = request.find('/?CMD=stop')

    #print("Data: " + str(CMD_forward))
    #print("Data: " + str(CMD_back))
    #print("Data: " + str(CMD_left))
    #print("Data: " + str(CMD_right))
    #print("Data: " + str(CMD_stop))

    if CMD_forward == 6:
        print('+forward')
        forward()
    if CMD_back == 6:
        print('+back')
        back()
    if CMD_left == 6:
        print('+left')
        left()
    if CMD_right == 6:
        print('+right')
        right()
    if CMD_stop == 6:
        print('+stop')
        stop()
    response = html
    conn.send(response)
    conn.close()
