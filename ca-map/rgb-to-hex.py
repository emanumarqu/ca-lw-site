#!/bin/python3

file = open("rgb-values.txt", "r")
for line in file.readlines():
    print('#%02x%02x%02x' % float(line))
file.close()