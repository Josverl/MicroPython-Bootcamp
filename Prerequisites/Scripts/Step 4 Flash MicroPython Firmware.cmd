
Set port=COM6

set PSRAM="N"
set Erase="N"

IF %PSRAM% == "Y" (
    ECHO "ESP32 PSRAM Version"
    pushd .\Firmware\MicroPython_LoBo_esp32_psram_all\esp32_psram_all

) ELSE (
    Echo ESP32 version
    pushd .\Firmware\MicroPython_LoBo_esp32_all\esp32_all
)


IF %Erase% == "Y" (
    esptool.py --port %port% erase_flash
)

esptool.py --chip esp32 --port %port%  --baud 921600 --before default_reset --after no_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x1000 ./bootloader/bootloader.bin 0xf000 phy_init_data.bin 0x10000 MicroPython.bin 0x8000 partitions_mpy.bin

popd
