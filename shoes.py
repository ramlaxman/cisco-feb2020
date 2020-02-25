#!/usr/bin/env python3


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': size}


shoes = [line_to_dict(one_line)
         for one_line in open('shoe-data.txt')]

shoes = sorted(shoes)

for one_shoe in shoes:
    print(one_shoe)


# (1) Sort the shoes by size (increasing order)
# (2) Sort the shoes, first by brand and then by size (within the brand)
# BONUS (3) Ask the user which field(s) they want to sort by, and sort by those
