
from mpu9250 import MPU9250

from my_mpu9250 import MPU9250
import sys
sys.modules
sys.modules.keys()

m = sys.modules['mpu9250']
help(m)

m2 = sys.modules['my_mpu9250']
help(m2)


#imported modules
import sys
modulenames = set(sys.modules)&set(globals())
allmodules = [sys.modules[name] for name in modulenames]

globals().items()

help(m)

MPU9250

help('modules')