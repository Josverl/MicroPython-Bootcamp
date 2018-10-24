
"""
Identifying the slowest section of code
This is a process known as profiling and is covered in textbooks and (for standard Python) 
supported by various software tools. For the type of smaller embedded application likely to 
be running on MicroPython platforms the slowest function or method can usually be established
by judicious use of the timing ticks group of functions documented in utime. 
Code execution time can be measured in ms, us, or CPU cycles.
The following enables any function or method to be timed by adding 
an @timed_function decorator:
"""
def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(myname, delta/1000))
        return result
    return new_func

import time, machine

@timed_function
def slow(x=1):
    import cmath
    for n in range(1000+x):
       cmath.sqrt(n)

slow()

slow(200)


""" 
The Native code emitter

This causes the MicroPython compiler to emit native CPU opcodes rather than bytecode. It covers the bulk of the MicroPython functionality, so most functions will require no adaptation (but see below). 
It is invoked by means of a function decorator:

@micropython.native
def foo(self, arg):
    buf = self.linebuf # Cached object
    # code
"""

@timed_function
def s2(x=1):
    slow2(x)

@micropython.viper
def slow2(x=1):
    import cmath
    for n in range(1000+x):
       cmath.sqrt(n)

s2()





ba = bytearray(10000)  # big array
func(ba[30:2000])      # a copy is passed, ~2K new allocation
mv = memoryview(ba)    # small object is allocated
func(mv[30:2000])      # a pointer to memory is passed

