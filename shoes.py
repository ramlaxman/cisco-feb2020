#!/usr/bin/env python3

import operator


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': size}


shoes = [line_to_dict(one_line)
         for one_line in open('shoe-data.txt')]


def by_size(shoe_dict):
    return shoe_dict['size']


def by_brand_and_size(shoe_dict):
    return shoe_dict['brand'], shoe_dict['size']


# shoes = sorted(shoes, key=by_size)
# shoes = sorted(shoes, key=by_brand_and_size)

user_fields = input("Enter field(s) for sorting: ").split()


# def by_user_choice(shoe_dict):
#     return shoe_dict[user_field]


# shoes = sorted(shoes, key=by_user_choice)

shoes = sorted(shoes, key=operator.itemgetter(user_field))

for one_shoe in shoes:
    print(one_shoe)


# (1) Sort the shoes by size (increasing order)
# (2) Sort the shoes, first by brand and then by size (within the brand)
# BONUS (3) Ask the user which field(s) they want to sort by, and sort by those
