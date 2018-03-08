
#Get the most recent MicroPython ESP32 firmeware from 

$folder = "C:\Dev\MicroPython-Bootcamp\PC\Prerequisites"

#Install Python 
#Python 32 & 4 bits installer
&$folder\jre-8u161-windows-x64.exe 
#todo Wait for it 



$64bit = $true
if ($64bit) { 

    &$folder\jre-8u161-windows-x64.exe 
} else {
    

    &$folder\jre-8u161-windows-i586.exe
}


