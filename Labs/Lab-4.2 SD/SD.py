import uos as os

def mountsd(addlib=True):
    #use SDCard 
    # SDCard configuration for M5Stack
    #todo check if device is already mounted
    #   os.umountsd()
    os.sdconfig(os.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
    os.mountsd()

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

