rem Installation of supporting Python modules 
rem 
rem 

#rem Note NO trailing backslash 
set folder = "C:\Dev\MicroPython-Bootcamp\PC\Prerequisites"

rem Install Pip using the get-pip script 
python %folder%\Get-pip.py

rem Serial and Serial over USB 
pip install pyserial

rem commandline tool to write or update firmware on a connected ESP32 ESP8622
pip install esptool

rem install remote shell for micropython 
pip install rshell 