#!/usr/bin/env python3


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': size}


[line_to_dict(one_line)
 for one_line in open('shoe-data.txt')]
