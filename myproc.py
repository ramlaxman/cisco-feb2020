#!/usr/bin/env python3

from multiprocessing import Process, Lock, Queue
from time import sleep
from random import randint

q = Queue()
l = Lock()


def hello(i):
    sleep(randint(0, 2))
    with l:
        print(f"{i} Hello!")
        print(f"{i} Goodbye!")
    q.put(i)


threads = []
for i in range(10):
    t = Thread(target=hello, args=(i,))
    t.start()
    threads.append(t)

# Make sure all threads are done by now
for one_thread in threads:
    one_thread.join()  # I'll wait/block until one_thread is complete


print("Done!")

# Now that they're done, grab things from the queue
while not q.empty():
    print(q.get())
