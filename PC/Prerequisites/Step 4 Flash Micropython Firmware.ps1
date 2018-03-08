#Get the most recent MicroPython ESP32 firmeware from 

$folder = "C:\Dev\MicroPython-Bootcamp\PC\Prerequisites"
$firmware = 'MicroPython_LoBo_esp32_psram_all\esp32_psram_all'
$port = 'Com8:'

#Find SerialPorts
function Get-SerialPorts()
{
    $RE_port = [regex]"\(COM(.*)\)"
    $SerialPorts = Get-WmiObject -Query 'SELECT * FROM Win32_PnPEntity WHERE ClassGuid="{4d36e978-e325-11ce-bfc1-08002be10318}"' | 
        Select Description, Name,  PNPClass , Service , Status | 
        ForEach-Object {
            #Split out the comport
            $re = $RE_port.Match($_.Name)

            $port = $re.Captures[0].value
            $port = $port.Substring( 1,$port.Length-2)
            Add-Member -InputObject $_ -MemberType NoteProperty -Name "Port" -Value $port -PassThru
    
        }
    return $SerialPorts
}


Get-SerialPorts


Push-Location

#CD to correct folder 
cd -Path (Join-Path $folder $firmware)

esptool.py --chip esp32 --port $port --baud 921600 --before default_reset --after no_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x1000 bootloader/bootloader.bin 0xf000 phy_init_data.bin 0x10000 MicroPython.bin 0x8000 partitions_mpy.bin

Pop-Location
#CD back 
