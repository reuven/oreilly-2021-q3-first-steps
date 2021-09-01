#!/usr/bin/env python3

def sum_numbers(*numbers):
    total = 0

    for one_number in numbers:
        total += one_number

    return total
