#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from time import sleep
from random import randint

q = Queue()


def hello(i):
    sleep(randint(0, 2))
    print(f"{i} Hello!")
    print(f"{i} Goodbye!")
    q.put(i)


threads = []
for i in range(10):
    t = Thread(target=hello, args=(i,))
    t.start()
    threads.append(t)

# Make sure all threads are done by now


print("Done!")

# Now that they're done, grab things from the queue
