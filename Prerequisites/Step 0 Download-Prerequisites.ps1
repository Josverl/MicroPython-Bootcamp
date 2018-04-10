
#Get the most recent MicroPython ESP32 firmeware from 

$folder = "C:\Dev\MicroPython-Bootcamp\Prerequisites"

#Use TLS 1.2
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12

function Download ($link, $folder)
{
    if (-not (Test-Path $folder)) {
        New-Item -Path $folder -ItemType Directory
    }
    if ($link) {
        $filename = join-path $folder (Split-path -Path $link -Leaf) 
        #download this file to the 
        Invoke-WebRequest -UseBasicParsing -Uri $link -OutFile $filename -Verbose
        Get-ChildItem $filename

        $ext = [System.IO.Path]::GetExtension($filename)

        if ($ext -ieq '.zip' ) {
            $DestinationPath = Join-Path $folder -ChildPath ([System.IO.Path]::GetFileNameWithoutExtension($filename))
            #extract the zip 
            Expand-Archive $filename -DestinationPath $DestinationPath -Force
        }
    }
}


$firmware = 'Loboris'
switch ($firmware)
{
    'Loboris' {
        
        #Get the current downloads 
        $downloads = Invoke-WebRequest 'https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/firmwares' -Verbose
 
        # MicroPython, single partition layout, 4MB Flash , ALL modules included ( Both non and including & 4MB SPIRAM)
        $ESP32_Builds = $downloads.Links | Where innertext -like "MicroPython*esp32*all"  

    }

    Default{
        #Get the current downloads 
        $downloads = Invoke-WebRequest http://micropython.org/download
        #Filter for the FIRST ESP32 DOWNLOAD 
        $ESP32_Builds = $downloads.Links | Where href -like "*esp32-*" | select -First 1
    }
}


foreach($build in $ESP32_Builds ) {
    Download -link $Build.href -folder (Join-Path $folder "Firmware")
} 

#Python 3

    #Get the current downloads 
    $downloads = Invoke-WebRequest 'https://www.python.org/downloads/release/python-364/'

    #Filter for the FIRST  DOWNLOAD 
    $Python3_link = $downloads.Links | Where-Object innertext -like "Windows x86-64 executable installer" | select -First 1

    if ($Python3_link) {
        Download -link $Python3_link.href -folder (Join-Path $folder "Python 3")

    } 


# PIP3
# Reference : https://arunrocks.com/guide-to-install-python-or-pip-on-windows/

#download `get-pip helper script 

Download -link 'https://bootstrap.pypa.io/get-pip.py' -folder  $folder 


#Silab USB Drivers 

$Silab_DL = "https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip"
Download -link $Silab_DL -folder (Join-Path $folder "USB")


#Java 
<#
    Java  files are downloaded manually 
    
    #Get the current downloads 
    $downloads = wget 'https://www.java.com/en/download/manual.jsp'

    #Filter for the DOWNLOAD 
    $Java_link = $downloads.Links | where innertext -like "Windows*Offline*" 
    $Java_link

    if ($Java_link) {
        foreach ($platform in $Java_link){ 
            Download -link $platform -folder $folder
        }

        #Install Python 
        #{sharedPath}python-3.6.3.exe /passive /quiet

    } 



        $filename = join-path $folder (Split-path -Path $link.href -Leaf) 
        #download this file to the 
        wget -UseBasicParsing -Uri $link.href -OutFile $folder

#>