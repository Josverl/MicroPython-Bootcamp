from machine import Pin, PWM
# Initialization
pwmFan = PWM(Pin(21), duty=0)
reverseFan = Pin(22, Pin.OUT)

# Turn Fan forward 70% speed
reverseFan.value(0)
pwmFan.duty(70)
# Decrease speed
pwmFan.duty(50)
# Decrease speed further (it might stop)
pwmFan.duty(30)

# Turn Fan backwards 70% speed
reverseFan.value(1)
pwmFan.duty(30)
# Decrease speed
pwmFan.duty(50)
# Decrease speed further (it might stop)
pwmFan.duty(70)

# Clean up
reverseFan(0)
pwmFan.deinit()