#!/usr/bin/python3
"""Prints numbers from 0 to 99."""
for i in range(100):
    if i == 99:
        print(i)
    else:
        print("{:02d},".format(i), end=" ")
