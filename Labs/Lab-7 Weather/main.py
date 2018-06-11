#main 
import time
if True:
    clock = time.strftime("%H:%M:%S",time.localtime())
    header('main.py               '+clock)
else:
    header('main.py')

#Run weatherstation demo
#exec(open('mystation.py').read(),globals())

log('Done ...')
