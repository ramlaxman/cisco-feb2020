#!/usr/bin/env python3

from threading import Thread


def hello():
    print("Hello!")


t = Thread(target=hello)
t.start()
