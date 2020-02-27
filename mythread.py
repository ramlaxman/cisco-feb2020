#!/usr/bin/env python3

from threading import Thread


def hello():
    print("Hello!")


for i in range(10):
    t = Thread(target=hello)
    t.start()
