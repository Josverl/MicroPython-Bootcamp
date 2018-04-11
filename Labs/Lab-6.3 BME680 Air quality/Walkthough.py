#Lab 6.3 walkthough 
#Only once 
#mkdir('/flash/lib')
cd('/flash/lib')
#copy the libraries
cd('/flash')

i2c_bus = I2CAdapter(sda=21,scl=22)
i2c_bus.scan()

#shoould show 
#>>> i2c_bus.scan()
#[104]


