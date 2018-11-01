#things to do 

VSCode walkthough 
=================

Lab 4
========
* rename folder / lab names (ie not start at 4.0 )
* AutoWiFi and phone browsers does not yet work 
* AutoWifi needs to wait a bit longer to connect to w10 hOTSPOT 
* review boot.py in 4.1 
    - Done :  Clean up where needed, copy all all next labs

Display code 
    - DONE : add preconfigured config file to connect 

* Demo 4
    - copy a number of labs from 4.1 to Demo-4.1
    - DONE : create demo 4.2 Modules
    - copy a number of labs from 4.3 to Demo-4.3

    DONE: Display Lab 4.3
        - Clean walkthrough
        - DONE Remove files from the testimages folder ( too slow to upload.... )
        - Document lab goals for 4.3 
            - Init display
            - write text 
            - draw line/ circle / triangle / square 
            - display image (jpg) [Scale image down] 
            

Helper Scrips and Snippets
==========================
* DONE: Wipe.py script to remove all files from device 

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

CHEATSHEET & Snippets 
======================
* Add a slide or line on the cheatsheet 
* where we point people to the snippets.py 

* Explain how to silence the High pitched beep 
    - caused by interference between 26 used for PWM and 25 (connected to speaker) 
    - silence by by pulling pin 25 to Low 



* FUTURE: Add a micropython snippets addin-to vscode ?

