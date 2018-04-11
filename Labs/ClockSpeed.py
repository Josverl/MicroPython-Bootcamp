'''
Show the difference of the 
https://loboris.eu/forum/Thread-Info-Power-Management
'''
import machine, time

def test_times(n):
   tstart=time.ticks_ms()
   a = 1.0
   for i in range(0, n):
       a += 1.23456
   ticks = time.ticks_diff(time.ticks_ms(), tstart)
   print("Freq={0:} MHz, time={1:} ms".format(machine.freq() // 1000000, ticks))
   return ticks

def test():
   start_fq = machine.freq() // 1000000
   for fq in (240, 160, 80):
       machine.freq(fq)
       time.sleep(1)
       test_times(500000)
   machine.freq(start_fq)

if sys.platform =='esp32_LoBo':
    print("starting clockspeeed / performance test") 
else:
    print("possibly unsupported platform") 
test()
  
