#!/usr/bin/env python3

from threading import Thread
from time import sleep
from random import randint


def hello(i):
    sleep(randint(0, 2))
    print(f"{i} Hello!")
    print(f"{i} Goodbye!")


for i in range(10):
    t = Thread(target=hello, args=(i,))
    t.start()
