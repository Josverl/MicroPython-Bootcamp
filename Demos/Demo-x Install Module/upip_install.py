import upip

##############################################
#  speed tests
##############################################
upip.install("micropython-pystone_lowmem")

#THis is the intended use 
import pystone_lowmem
import machine
#Only frequencies (2) 80Mhz, 160MHz, 240MHz
for mhz in (80,160,240):
    machine.freq(mhz)
    print( "testing at {}Mhz".format(mhz))
    pystone_lowmem.main()


#One thing leads to another 
upip.install("micropython-timeit")


#Also 'micropython-getopt', 'micropython-itertools', 'micropython-linecache', 'micropython-time', 'micropython-traceback'
import ffilib as ffi
import timeit

## But dont know how to use it :-( .....
"""
setup = '''
import random

random.seed('slartibartfast')
s = [random.random() for i in range(1000)]
timsort = list.sort
'''
print( min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000)) )
"""