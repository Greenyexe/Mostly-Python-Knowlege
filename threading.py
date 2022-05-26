# thread = a flow of execution. Like a separate order of instructions.
# However each thread takes a turn running to achieve concurrency
# GIL = (global interpreter lock), allows only one thread to hold the control of the python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
# use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user inputs, web scraping)
# use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")
def drink_tea():
    time.sleep(4)
    print("You drank your tea")
def study():
    time.sleep(5)
    print("You finished your studying! ;)")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_tea, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()

#eat_breakfast()
#drink_tea()
#study()

print(threading.active_count()) # was first displayed first because its part of the main thread
print(threading.enumerate())
print(time.perf_counter())