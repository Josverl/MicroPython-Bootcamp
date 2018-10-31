#detect touch input
# Only on Pin 2 - this is the only exposed touch input  

def test_touch():
    while True:
        lastx = 0
        lasty = 0
        t,x,y = tft.gettouch()
        if t:
            dx = abs(x-lastx)
            dy = abs(y-lasty)
            if (dx > 2) and (dy > 2):
                tft.circle(x,y,4,tft.RED)
        time.sleep_ms(50)

