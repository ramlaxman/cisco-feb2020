#!/usr/bin/env python3

from multiprocessing import Process, Lock, Queue
from time import sleep
from random import randint

q = Queue()
l = Lock()


def hello(i):
    sleep(randint(0, 6))
    with l:
        print(f"{i} Hello!")
        print(f"{i} Goodbye!")
    q.put(i)


processes = []
for i in range(10):
    p = Process(target=hello, args=(i,))
    p.start()
    processes.append(p)

# Make sure all threads are done by now
for one_process in processes:
    one_process.join()  # I'll wait/block until one_thread is complete


print("Done!")

# Now that they're done, grab things from the queue
while not q.empty():
    print(q.get())
