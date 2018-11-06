
#import or install and import asyncio
try:
    import uasyncio as asyncio
except:
    import upip
    upip.install("micropython-uasyncio")
    import uasyncio as asyncio

loop = asyncio.get_event_loop()
async def bar():
    count = 0
    while True:
        count += 1
        print(count)
        await asyncio.sleep(1)  # Pause 1s

def foo(x):
    print('Foooo {}'.format(x))

loop.call_soon(foo, 42) # Schedule callback 'foo' ASAP with an arg of 5.
loop.call_later(2, foo, 2000) # Schedule after 2 seconds.
loop.call_later_ms(50, foo, 50) # Schedule after 50ms.
loop.run_forever()


loop.create_task(bar()) # Schedule ASAP
loop.run_forever()
