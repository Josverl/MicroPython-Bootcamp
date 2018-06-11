#main 
import time
if True:
    clock = time.strftime("%H:%M:%S",time.localtime())
    header('main.py               '+clock)
else:
    header('main.py')

#Run menu
exec(open('menuv1.py').read(),globals())

log('Done ...')

