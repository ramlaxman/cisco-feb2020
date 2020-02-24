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
