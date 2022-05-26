#*****************************
# Python Multiprocessing
#*****************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
# multiprocessing = better for cpu bound tasks (heavy cpu usage)
#multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count +=1

def main():
    print(cpu_count())
    
    start = time.perf_counter()
    a = Process(target=counter, args=(166666666,)) # need the commer after the billion to make a tuple
    a.start()

    b = Process(target=counter, args=(166666666,)) # need the commer after the billion to make a tuple
    b.start()

    a.join()
    b.join()
    
    c = Process(target=counter, args=(166666666,)) # need the commer after the billion to make a tuple
    c.start()

    d = Process(target=counter, args=(166666666,)) # need the commer after the billion to make a tuple
    d.start()

    c.join()
    d.join()

    e = Process(target=counter, args=(166666666,)) # need the commer after the billion to make a tuple
    e.start()

    f = Process(target=counter, args=(166666666,)) # need the commer after the billion to make a tuple
    f.start()

    e.join()
    f.join()

    print("Finished in:", time.perf_counter()-start, "seconds")

if __name__ == "__main__": # needed for windows
    main()  