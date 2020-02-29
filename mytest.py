#!/usr/bin/env python3


def hello(name: str) -> str:
    greeting = 3
    greeting = 'Hello'
    return f'{greeting}, {name}'


print(hello('world'))
print(hello(5))
print(hello([10, 20, 30]))
