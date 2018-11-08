# My first script that loads another module
import module

#lets see what this module offers 
help(module)

#do some work
r = module.dowork(4,2)
print(r)


print( module.greeting('Marcus') )
