# --------------------------------------------------------------------------
# Will fail unless you have the path addedd to the system module load path ( )
import structured

# --------------------------------------------------------------------------
# lets look on the device itself
# load some additional commands ( MicroPython Shell a.k.a. upysh )
from upysh import * 
ls
ls('/slash/lib')

# --------------------------------------------------------------------------
# Note:  the module is not in the current directory but in a subolder, 
# how do we load it ?
import sys
print("The module search path is" , sys.path)

# --------------------------------------------------------------------------
# let's adjust the path to the correct location on the flash 
sys.path[1]='/flash/lib'

# --------------------------------------------------------------------------
#and try again 
import structured
help(structured)

# --------------------------------------------------------------------------
# A module can also be compiled and loaded as a script 
# Note this will use up additional memory, so it is not generally advisable
exec( open('/flash/lib/structured.py').read() , globals() )
