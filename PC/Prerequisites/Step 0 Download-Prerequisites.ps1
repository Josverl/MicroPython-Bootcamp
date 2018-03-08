
#Get the most recent MicroPython ESP32 firmeware from 

$folder = "C:\Dev\MicroPython-Bootcamp\PC\Prerequisites"


function Download ($link, $folder)
{
    #Use TLS 1.2
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
    if (-not (Test-Path $folder)) {
        New-Item -Path $folder -ItemType Directory
    }
    if ($link) {
        $filename = join-path $folder (Split-path -Path $link -Leaf) 
        #download this file to the 
        wget -UseBasicParsing -Uri $link -OutFile $filename -Verbose
        dir $filename

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
        $downloads = wget 'https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/firmwares' -Verbose
 
        # MicroPython, single partition layout, 4MB Flash & 4MB SPIRAM, ALL modules included
        $ESP32_link = $downloads.Links | where innertext -like "MicroPython*esp32*psram*all"  | select -First 1

    }

    Default{
        #Get the current downloads 
        $downloads = wget http://micropython.org/download
        #Filter for the FIRST ESP32 DOWNLOAD 
        $ESP32_link = $downloads.Links | where href -like "*esp32-*" | select -First 1
    }
}


if ($ESP32_link) {
    Download -link $ESP32_link.href -folder $folder
} 

#Python 3

    #Get the current downloads 
    $downloads = wget 'https://www.python.org/downloads/release/python-364/'

    #Filter for the FIRST ESP32 DOWNLOAD 
    $Python3_link = $downloads.Links | where innertext -like "Windows x86-64 executable installer" | select -First 1

    if ($Python3_link) {
        Download -link $Python3_link.href -folder $folder

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