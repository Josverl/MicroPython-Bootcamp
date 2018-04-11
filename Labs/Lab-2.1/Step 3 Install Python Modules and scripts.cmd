rem Installation of supporting Python modules 
rem 
rem commandline tool to write or update firmware on a connected ESP32 ESP8622
pip install esptool

rem install remote shell for micropython 
pip install rshell 

rem Add the path to the PIP installed modules (and included scripts)
Rem 
rem SETX PATH "%PATH%;%LOCALAPPDATA%\programs\python\python36\lib\site-packages

Rem add the .py extention as an executable extention
Rem 
Rem SETX PATHEXT "%PATHEXT%;.PY"

