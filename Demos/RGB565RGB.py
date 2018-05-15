"""
    Convert between 16 bit and 24 bit RGB values 
"""
def RGB565toRGB(Pixel):
    if Pixel is None:
        r = 0
    else:
        #Colors RGB565  5 + 6 + 5 = 16 bit
        mred = const(0b1111100000000000)
        mgrn = const(0b0000011111100000)
        mblu = const(0b0000000000011111)
        #Isolate the RGB Values and scale them 
        #todo: improve scaling to 255 / FF 
        red = ((mred & Pixel) >>11) *8
        grn = ((mgrn & Pixel) >>5 ) *4
        blu =  (mblu & Pixel) * 8
        r = red << 16 | grn<<8 | blu
    return r

def RGBtoRGB565(Pixel):
    if Pixel is None:
        r = 0
    else:
        #RGB 24 = 3 x 8
        mred8 = const(0xFF0000)
        mgrn8 = const(0x00FF00)
        mblu8 = const(0x0000FF)
        #Isolate the RGB Values and downscale them to 565 
        red = ((mred8 & Pixel) >>16)>>3
        grn = ((mgrn8 & Pixel) >>8 )>>2
        blu = (mblu8 & Pixel) >>3
        #print(red,grn,blu)
        #leftshift and combine in rgb565 
        r = red<<11 | grn<<5 |blu
    return r 
