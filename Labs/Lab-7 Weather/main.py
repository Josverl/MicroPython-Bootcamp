#main 
if True:
    clock = time.strftime("%H:%M:%S",time.localtime())
    header('main.py               '+clock)
else:
    header('main.py')

#import publishThingspeak

#Run wetherstation demo
#exec(open('stationtemplate.py').read(),globals())

log('Done ...')
