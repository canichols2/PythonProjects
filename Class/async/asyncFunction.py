import asyncio
import threading as th
import datetime

async def wait_seconds(second):
    await asyncio.sleep(second)

async def write_message(num, loop):
    end_time = loop.time() + 30.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await wait_seconds(5)

async def new_message(loop):
    end_time = loop.time() + 10.0
    x = 0
    while True:
        print("[{}]-Hello World".format(x))
        x += 1
        if (loop.time() + 1.0) >= end_time:
            break
        await wait_seconds(2)


# Expected Result:
#   Each of the first two method calls will 
#   execute in the loop, and the last one will start
#   after the first run_forever finishes and when the
#   second run_forever starts
# Actual Result:
#   Using "run_forever()" doesn't 
#   let the code continue after loop is complete
loop = asyncio.get_event_loop()

asyncio.ensure_future(write_message(1,loop))
asyncio.ensure_future(new_message(loop))
print("starting First Run_Forever()")
loop.run_forever()
print("Finished First Run_Forever()")


print("Adding new ensure_future to same loop")
asyncio.ensure_future(write_message(2,loop))
print("Starting Second Run_Forever() call on same loop")
loop.run_forever()
print("Finished Second Run_Forever()")
