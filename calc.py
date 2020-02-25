#!/usr/bin/env python3


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


ops = {'+': add,
       '-': sub,
       '*': mul,
       '/': div}

while True:
    s = input("Enter an expression: ").strip()

    if not s:
        break

    if not s.count(' ') == 2:
        print("Wrong number of words; try again")
        continue

    first, op, second = s.split()

    if op in ops:
        print(ops[op](int(first), int(second)))
    else:
        print(f"No operator {op}")
