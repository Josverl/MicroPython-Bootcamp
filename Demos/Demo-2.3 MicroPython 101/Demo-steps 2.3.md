# Demo Walkthough

## Hard & Software Needed

1. Three Color Led attached to Port A and Port B 

2. WebCam  to show the Led Status 
 

## Prepare 

1. Open this _folder_ in VSCode
    Note: make sure to open the folder otherwise the upload will not work
2. Use `PyMakr > Upload project` to upload all files [optional]
3. Connect the Led 
    - Port A 
        - 21 = white  ==> Blue Led 
        - 22 = yellow ==> Red Led
        - 0v = black  ==> 
        - 5v = red    ==> 
    - PORT B
        - 26 = white  ==> Green Led 
        - 36 = yellow ==> 
        - 0v = black  ==> 
        - 5v = red    ==> 


## Walkthrough

### Show LED control of a single / multiple LEDs 
1. Boot MCU 
2. Show the Led status, 
    - note that [it is / they are] glowing faintly already before doing anything
    - explain the pins are in a `floating` state ,and that this allows some current to flow  
3. open the file led-Signal.py 
    - refer to the comments to run the relevant section of the file step-by-step
    - use `Ctrl-Shift-Enter` or `Right-Click>Run Current Selection`


### Get a File from a web server
1. Boot MCU 
2. Verify that it connects to the network 
3. Open getfile.py
4. run the file 
5. show the output / file content that was retrieved from the werb server.

### Unique identier 
1. Open UniqueID.py
2. run the file 
3. Show that there is a unique ID can use 



