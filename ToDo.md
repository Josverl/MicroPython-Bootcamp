#things to do 

Uodate lab 4.x Button detection 

* AutoWiFi and phone browsers does not yet work reliable
* autowifi has an error
```
        Connect to Wifi ssid:M5Stack-9115
        And connect to esp via your web browser (like 192.168.4.1)
        listening on ('0.0.0.0', 80)
        Traceback (most recent call last):
        File "boot.py", line 20, in <module>
        File "/flash/lib/wifisetup.py", line 63, in auto_connect
        File "/flash/lib/wificonfig.py", line 152, in webserver_start
        OSError: Wifi Invalid Argument
```
    - Document lab goals for 4.3 
        - Init display
        - write text 
        - draw line/ circle / triangle / square 
        - display image (jpg) [Scale image down] 

WeatherStation 
- Extract Demos from LAB 7 
    - PIR Loop
- Seperate


CHEATSHEET & Snippets 
======================
* Add a slide or line on the cheatsheet 
* where we point people to the snippets.py 



Helper Scrips and Snippets
==========================
* Document Error messages 
    import uerrno
    help (uerrno)

        EPERM -- 1
        ENOENT -- 2
        EIO -- 5
        EBADF -- 9
        EAGAIN -- 11
        ENOMEM -- 12
        EACCES -- 13
        EEXIST -- 17
        ENODEV -- 19
        EISDIR -- 21
        EINVAL -- 22

        OSError: 23 - Sockets left open ?
        OSError: 28 - writing binary data to file ?
        EOPNOTSUPP -- 95
        EADDRINUSE -- 98

        ECONNABORTED -- 103
        ECONNRESET -- 104
        ENOBUFS -- 105
        ENOTCONN -- 107
        ETIMEDOUT -- 110
        ECONNREFUSED -- 111
        EHOSTUNREACH -- 113
        EALREADY -- 114
        EINPROGRESS -- 115

    import os 
    TODO: Were are the other errors code 
        * Add list of error codes ( I have already created that somewhere ....?)


* FUTURE: Add a micropython snippets addin-to vscode ?


