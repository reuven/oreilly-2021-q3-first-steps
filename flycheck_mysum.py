#!/usr/bin/env python3

def sum_numbers(*numbers):
    total = 0

    for one_number in numbers:
        total += one_number

    return total


print(sum_numbers(10, 20, 30))
print(sum_numbers(10.5, 20, 30))
print(sum_numbers('a', '20, 30))

