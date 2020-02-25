#!/usr/bin/env python3

import operator


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}

while True:
    s = input("Enter an expression: ").strip()

    if not s:
        break

    if not s.count(' ') == 2:
        print("Wrong number of words; try again")
        continue

    first, op, second = s.split()

    if not first.isdigit():
        print(f'{first} is not numeric')
        continue
    if not second.isdigit():
        print(f'{second} is not numeric')
        continue

    if op in ops:
        print(ops[op](int(first), int(second)))
    else:
        print(f"No operator {op}")
