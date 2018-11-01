import machine, time, ustruct

# Initialize serial connection toMCU680 
uart = machine.UART(1, tx=26, rx=36, baudrate=9600)

# Variables
measurements = bytearray(20)

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)


def init_sensor():
    # Initialize GY_MCU680 to output all data
    _ = uart.write(b'\xa5\x55\x3f\x39') 
    # Initialize GY_MCU680 in continuous output mode
    _ = uart.write(b'\xa5\x56\x02\xfd')

def process_data(measurements):
        results = {}
#       temp2=(Re_buf[4]<<8|Re_buf[5]);   
        Temp = measurements[4] << 8 | measurements[5]
        results.update({'Temp' : Temp})       
#       temp1=(Re_buf[6]<<8|Re_buf[7]);
        Humi = measurements[6] << 8 | measurements[7]
        results.update({'Humi' : Humi})
#       Pressure=((uint32_t)Re_buf[8]<<16)|((uint16_t)Re_buf[9]<<8)|Re_buf[10];
        Pres = measurements[8] << 16 | measurements[9] << 8 | measurements[10]
        results.update({'Pres' : Pres})        
#       IAQ_accuracy= (Re_buf[11]&0xf0)>>4;
        IAQa = measurements[11] & int('f0',16) >> 4
        results.update({'IAQa' : IAQa})        
#       IAQ=((Re_buf[11]&0x0F)<<8)|Re_buf[12];
        IAQ = measurements[11] & int('f0',16) << 8 | measurements[12]
        results.update({'IAQ' : IAQ})        
#       Gas=((uint32_t)Re_buf[13]<<24)|((uint32_t)Re_buf[14]<<16)|((uint16_t)Re_buf[15]<<8)|Re_buf[16];
        Gas = measurements[13] << 24 | measurements[14] << 16 | measurements[15] << 8 | measurements[16]
        results.update({'Gas' : Gas})
#       Altitude=(Re_buf[17]<<8)|Re_buf[18]; 
        Alt = measurements[17] << 8 | measurements[18]
        results.update({'Alt' : Alt})    
        return results

init_sensor()


#uart.flush()
while True:
    #Wait for at least 20 bytes waiting
    buffer_size = uart.any()
    if buffer_size >= 20:
        #now get exactly 20 bytes (length of the buffer) 
        uart.readinto(measurements)
        #transfor the data into a dict 
        readings = process_data(measurements)
        #print the dict 
        print(readings)
        #ToDo : Add Fancy Print 
        print("Temperature : {Temp}, Pressure {Pres}".format( **readings))

    time.sleep(0.1)

#        print("Type1: ", type(measurements[2][2]))   -> 'str'
#        print("Type2: ", type(ustruct.unpack('b',measurements[2][2])))     -> 'tuple'
#        print("Type3: ", type(ustruct.unpack('b',measurements[2][2])[0] ))  -> 'int'

# Meaning of the Byte0:
# Bit7 Bit6 Bit5     Bit4 Bit3 Bit2         Bit1     Bit0
# NC   NC   altitude Gas  IAQ  Air pressure Humidity Temperature
# 
# Bit6~Bit7 Reserved 
# Bit5 This bit is 1 for output altitude data and 0 for no output.
#  (The data type is signed 16 bits: -32768----- 32767, unit m) 
# Bit4 The position 1 indicates the output Gas data, 0 has no output;
#  Gas indicates the gas resistance resistance value, which decreases with the increase of the
#  gas concentration. small. (The data type is unsigned 32 bits: 0----- 4294967296, unit ohm)
# Bit3 This bit is 1 to indicate IAQ data output, 0 is no output; 
#  IAQ is for indoor air quality. The range of IAQ is 0~500. The larger the value, the worse 
#  the air quality. The IAQ data type is unsigned 16 bits, with the first 4 bits indicating 
#  the accuracy of the sensor's IAQ and the last 12 bits representing the IAQ value.
# Bit2 This position 1 indicates the output air pressure data, 0 has no output;
#  Data range: 300~110000, unit Pa; (The data type is unsigned 24 bits) 
# Bit1 This bit is set to 1 to indicate the humidity data after the output is magnified 100 times.
#  Data range: 0~100, unit %rH (ie relative humidity); 
#  (The data type is unsigned 16 bits) 
# Bit0 The position 1 indicates the temperature data after the output is amplified 100 times
#  and 0 has no output; Temperature range: -40~85, unit °C; 
#  (The data type is signed 16 bits: -32768----- 32767)

# I tried to test byte 0 but the value is always the same :-(
#        if testBit(ustruct.unpack('B',measurements[2][0])[0], 0) != 0:
#            print("Has Temperature (range -40 - 85 °C)")
#        if testBit(ustruct.unpack('B',measurements[2][0])[0], 1) != 0:
#            print("Has Relative humidity (range 0 - 100%")
#        if testBit(ustruct.unpack('B',measurements[2][0])[0], 2) != 0:
#            print("Has Air pressure")
#        if testBit(ustruct.unpack('B',measurements[2][0])[0], 3) != 0:
#            print("Has Indoor Air Quality (IAQ range is 0~500. The larger the value, the worse the air quality qualidade)")
#        if testBit(ustruct.unpack('B',measurements[2][0])[0], 4) != 0:
#            print("  Tem resistancia de Gas")
#        if testBit(ustruct.unpack('B',measurements[2][0])[0], 5) != 0:
#            print("  Tem Altitute")


# Arduino code
#  temp2=(Re_buf[4]<<8|Re_buf[5]);   
#  Temperature=(float)temp2/100;
#  temp1=(Re_buf[6]<<8|Re_buf[7]);
#  Humidity=(float)temp1/100; 
#  Pressure=((uint32_t)Re_buf[8]<<16)|((uint16_t)Re_buf[9]<<8)|Re_buf[10];
#  IAQ_accuracy= (Re_buf[11]&0xf0)>>4;
#  IAQ=((Re_buf[11]&0x0F)<<8)|Re_buf[12];
#  Gas=((uint32_t)Re_buf[13]<<24)|((uint32_t)Re_buf[14]<<16)|((uint16_t)Re_buf[15]<<8)|Re_buf[16];
#  Altitude=(Re_buf[17]<<8)|Re_buf[18]; 
