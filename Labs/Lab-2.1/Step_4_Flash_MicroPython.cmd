@Echo off 
Rem Change the port to match the USB serial port 
Set port=COM6

rem PSRAM defines the pre-built firmware version selected 
Rem Y or N 
set PSRAM="N"


rem Erase the flash (required for 1st time only) 
Rem Y or N 
set Erase_FLASH="Y"

IF %Erase_FLASH% == "Y" (
    esptool.py --port %port% erase_flash
)

Set PreReq="C:\MicroPython-Bootcamp\PreRequisites"

IF %PSRAM% == "Y" (
    ECHO "ESP32 PSRAM Version"
    pushd %PreReq%\Firmware\MicroPython_LoBo_esp32_psram_all\esp32_psram_all

) ELSE (
    Echo ESP32 version
    pushd %PreReq%\Firmware\MicroPython_LoBo_esp32_all\esp32_all
)


Rem The Flash Command as specified for the lobo firmware, tweaked the bootloader path for windows
esptool.py --chip esp32 --port %port%  --baud 921600 --before default_reset --after no_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x1000 ./bootloader/bootloader.bin 0xf000 phy_init_data.bin 0x10000 MicroPython.bin 0x8000 partitions_mpy.bin

popd
