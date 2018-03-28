from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_5_secs(message):
    sleep(5)
    return message
 
pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_5_secs, ("hello"))

# Future objects contain properties and methods
# such as done to tell if it got it's response 
# and the actual response using result()
print(future.done())
sleep(5)
print(future.done())
print(future.result())