#Main
import os,sys

def mountsd():
    #use SDCard 
    # SD Card configuration for LoLin32 Pro in SPI mode
    os.sdconfig(os.SDMODE_SPI, clk=14, mosi=15, miso=2, cs=13)
    os.mountsd()
    
    try:
        #create Library for modules 
        os.mkdir('/sd/lib')
    except:
        pass
    sys.path.append('/sd/lib')


def demo1():
    import curl
    response = curl.get('loboris.eu/ESP32/info.txt')
    #response[0]                #return code 
    #print(response[1])         #headers
    print(response[2])          #body

print('Main: ready to start doing things')
mountsd()

sys.path
help(os)


os.chdir('/flash')
help('modules')

