import upip, os,sys

#make sure there is a folder to store the module package into 
try: os.mkdir(sys.path[1])
except: pass

#This should work but fails on LoBo 
upip.install("micropython-pystone_lowmem")

#Debuggin on , but no additional info
upip.debug = True
upip.install("micropython-pystone_lowmem")

#this function appears to throw the error 
upip.get_pkg_metadata("micropython-pystone_lowmem")


#Try workaround 
import upip2
#but this fails as well 
upip2.get_pkg_metadata("micropython-pystone_lowmem")


#THis is the intended use 
import pystone_lowmem
pystone_lowmem.main()
