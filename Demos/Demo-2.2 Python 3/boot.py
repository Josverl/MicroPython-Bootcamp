# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal
print("-- performing boot --")

# acces the (ESP32) hardware functionality using the machine library 
import machine 
# read the 
reset , wake = machine.wake_reason()

#as an exaple it is possible to determine how/why the microcontroller was started or woken up 
if reset == 0:
    print('Power On')
elif reset == 1:
    print('Hard reset')
elif reset == 6:
    print('Soft reset')

if wake == 3:
    print('woken by Touchpad')

print("-- end of boot.py --")
