# Demo Walkthough

## Hard & Software Needed

1) M5Stack Basic or Fire with LoBo fIRMWARE
2) VSCode and Pymakr add-in
3) [Optional] WebCam if you want to show the M5 Display output
 
## Prepare 

1. Remove all files from flash (using wipe.py script)
2. Open this _folder_ in VSCode

    Note: make sure to open the folder otherwise the upload will not work

## Walkthrough

1. Point out different files 
    -  boot.py
        briefly explain that this is started first 
    -  main.py 
        briefly explain that this is started after boot.py has competed
2. Upload all files, explain that the files are now stored on the 'flash drive' of the MCU
3. Show the execution on powerup / restart  
    - open the terminal window (PyCom Console)
    - Reboot the MCU usign the poweron button
    - watch the messages, see Boot and Main 
```
            ---performing boot---
            Power On
            ---end of boot.py---
            -- main.py --
            Hello world 0
            Hello world 1
            Hello world 2
            -- end of main.py --
            MicroPython ESP32_LoBo_v3.2.24 - 2018-09-06 on ESP32 board with ESP32
            Type "help()" for more information.
            >>>
 ```
4. Open the GameOfLife.py file in vscode 
    - Explain that this is a simple biology simulation 
    - run the script usign the PyMakr>Run (`Ctrl-Shift-R`)
    - show the terminal window (PyCom Console)


5. [Optional] Open the GameOfLife-M5.py file in vscode 
    - Explain that this hhas a few additions to allow it to write to the M5Stack screen  
    - Show the script section with display init `#Additions for M5Stack Display`
    - run the script usign the PyMakr>Run (Ctrl-Shift-R)
    - show the terminal window (PyCom Console)
    - Show the difference between display and fastdisplay 
















