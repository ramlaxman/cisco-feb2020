#!/usr/bin/env python3

import random


def create_password_maker(s):
    def inner(n):
        output = ''
        return output
    return inner


make_simple_password = create_password_maker('abcdefg')
make_crazy_password = create_password_maker('abcdef!@#$%')

my_new_pw = make_simple_password(10)
my_new_tough_pw = make_crazy_password(50)

print(my_new_pw)
print(my_new_tough_pw)
