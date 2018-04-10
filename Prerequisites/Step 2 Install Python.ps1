
#Assume current folder

#Install Python 
#Python 32 & 4 bits installer
.\Python\python-3.6.4-amd64.exe /passive

Start-Process -Wait -FilePath .\Python\python-3.6.4-amd64.exe -ArgumentList '/passive' 

# Make sure that the python scripts can be found (current Session)
$ENV:PATH="$ENV:PATH;$env:APPDATA\Python\Python36\scripts"

#capture the original path that needs to be modified: As Admin 
# todo: Elevate to admin 
$oldpath = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
if ($oldpath.Contains(";$env:APPDATA\Python\Python36\scripts") -eq $false){
    $newpath = "$oldpath;$env:APPDATA\Python\Python36\scripts"
    Set-ItemProperty -Path ‘Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment’ -Name PATH -Value $newPath
}


<#
Next, set the system’s PATH variable to include directories that include Python components and packages we’ll add later. To do this:
Open the Control Panel (easy way: click in the Windows search on your task bar and type “Control Panel” then click the icon).
In the Control Panel, search for Environment; click Edit the System Environment Variables. Then click the Environment Variables button.
In the User Variables section, we will need to either edit an existing PATH variable or create one. If you are creating one, make PATH the variable name and add the following directories to the variable values section as shown, separated by a semicolon. 
If you’re editing an existing PATH, the values are presented on separate lines in the edit dialog. Click New and add one directory per line
#>


$64bit = $true
if ($64bit) { 
    #do not use /s option as this does not provide any user feedback
    Start-Process -Wait -FilePath .\Java\jre-8u161-windows-x64.exe

} else {
    Start-Process -Wait -FilePath .\Java\jre-8u161-windows-i586.exe
}


