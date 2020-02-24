#!/usr/bin/env python3

# dictdiff takes two dicts as arguments
# it returns a dict representing the difference between them
# if a key-value pair exists (identical) in both, ignore it in the output
# if a key exists in both, with different values, return
#   a key-value pair with the key and a list as the value, with
#   the elements [first, second]
# if a key exists in just one, return None as the value


def dictdiff(first, second):
    output = {}
    for one_key in first.keys() | second.keys():
        v1 = first.get(one_key)
        v2 = second.get(one_key)

        if v1 != v2:
            output[one_key] = [v1, v2]

    return output


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}

print(dictdiff(d1, d1))
# prints {}

print(dictdiff(d1, d2))
# # # # # prints {'c': [3, 4]}

d1 = {'a': 1, 'b': 2, 'd': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}

print(dictdiff(d1, d2))
# # # # # prints {'c': [None, 4], 'd': [3, None]}

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'd': 4}

print(dictdiff(d1, d2))
# # # prints {'c': [3, None], 'd': [None, 4]}
