
#oneWire thermometer(s)
import machine, m5stack
ow = machine.Onewire(5)
ow.scan()


        
# the onewire data line is on GPIO12
data = machine.Pin(5)
if True:
    #ESP32_LoBO
    ow = machine.Onewire(5)
    ds = machine.Onewire.ds18x20(ow, 0)
else :
    #standard MicroPython
    import onewire, ds18x20
    ow = onewire.OneWire(data)
    ds = ds18x20.DS18X20(ow)

ow.scan()    
ow
#and the temp sensors
ds.convert_read()

