#!/usr/bin/env python3


class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop of {self.flavor}'


class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        self.scoops += args[:self.max_scoops - len(self.scoops)]
#         for new_scoop in args:
#             if len(self.scoops) >= Bowl.max_scoops:
#                 break
#             self.scoops.append(new_scoop)

    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]

    def __repr__(self):
        output = 'Bowl of:\n'
        output += '\n'.join([f'\t{i}: {one_scoop}'
                             for i, one_scoop in enumerate(self.scoops, 1)])
        return output


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

b = Bowl()
b.add_scoops(s1, s2)  # notice: different number of scoops
b.add_scoops(s3)  # in each call to add_scoops
b.add_scoops(s4, s5)
print(b.flavors())   # return a string of flavors from the scoops


class BigBowl(Bowl):
    max_scoops = 5


bb = BigBowl()
bb.add_scoops(s1, s2)  # notice: different number of scoops
bb.add_scoops(s3)  # in each call to add_scoops
bb.add_scoops(s4, s5)
print(bb.flavors())   # return a string of flavors from the scoops


# Create a BigBowl class
# with a max of 5 scoops
# - reuse as much code as possible
# - but also make sure that each class continues to work

print(s1)
print(b)
print(bb)
