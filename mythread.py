#!/usr/bin/env python3

from threading import Thread


def hello(i):
    print(f"{i} Hello!")


for i in range(10):
    t = Thread(target=hello, args=(i,))
    t.start()
