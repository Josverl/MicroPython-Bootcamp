#import the module using a different name
import module as mod

#now we can us a different name to get to the immported functions
mod.dowork(2,3)

# the original module and filename are still present
help(mod)

#NOTE: the __file__ name 
