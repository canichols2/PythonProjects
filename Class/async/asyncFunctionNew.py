import asyncio
from threading import Thread
import datetime
import time

async def wait_seconds(second):
    await asyncio.sleep(second)

async def write_message(num, loop):
    end_time = loop.time() + 30.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await wait_seconds(1)

async def new_message(loop):
    end_time = loop.time() + 10.0
    x = 0
    while True:
        print("[{}]-Hello World".format(x))
        x += 1
        if (loop.time() + 1.0) >= end_time:
            break
        await wait_seconds(.5)



# Expected Result:
#   With runnin the loop in a separate thread
#   I will be able to add methods to it after 
#   I call the run_forever
# Actual Result:
#   Starting the run_forever loop in another thread
#   allows me to get the current "queued" method's
#   running while I continue to add more methods
#   to the queue.
#   -------------
#   I also needed to add a loop at the end so the main thread doesn't exit before the child thread finishes. .
loop = asyncio.get_event_loop()

def runFunction(lp):
    lp.run_forever()

asyncio.ensure_future(write_message(1,loop))
asyncio.ensure_future(new_message(loop))

print("creating thread for Run_Forever()")
thread = Thread(target=runFunction, args=(loop, ))

print("starting thread for Run_Forever()")
thread.start()
# thread.join()

print("Finished starting thread for Run_Forever()")
time.sleep(10)
print("Adding new ensure_future to same loop")
asyncio.ensure_future(write_message(2,loop))

# Without while true to keep main thread open,
#   The program just exits and the loop ends.
#   -------------------------------------------
#   thread.join() also causes the main thread not to exit
#   but kind of does the same thing as if not using threads.
#   The run_forever() loop will then just sit in the main thread. 
#   This is essentially what I am doing anyway though with the while true here
#   I can just add the join() function to the end instead of in the middle
#   to have the same outcome..
end = False
# while True:
#     time.sleep(5)
#     if (end):
#         break
thread.join()

# Still, it would be great to find a new method
#   besides calling run_forever() such as run_until_complete()
#   or something like that.