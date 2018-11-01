# mount SDCard 
# SDCard configuration for M5Stack
import uos as os

def mountsd(addlib=True):
    #use SDCard 
    # SDCard configuration for M5Stack
    try:
        #crude way to detect if the sd is already loaded 
        _ = os.stat('/sd')
    except:
        #if 
        _ = os.sdconfig(os.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
        _ = os.mountsd()

    if addlib: 
        #very simple , just try to create and add the /sd/lib folder to the path
        #create Library for modules on the sd card 
        try:
            os.mkdir('/sd/lib')
        except:
            pass
    #if exist
    sys.path.append('/sd/lib')

mountsd(addlib=True)

