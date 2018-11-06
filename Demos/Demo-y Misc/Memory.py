#Report Memory 

'''
 Reset reason: RTC WDT reset
    uPY stack: 19456 bytes
     uPY heap: 512256/6240/506016 bytes (in SPIRAM using malloc)
'''


import gc
import micropython

#gc.collect()
micropython.mem_info()
print('-----------------------------')
print('Initial free: {} allocated: {}'.format(gc.mem_free(), gc.mem_alloc()))


micropython.mem_info()

dir(gc)
dir(micropython)