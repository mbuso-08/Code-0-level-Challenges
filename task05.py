import argparse
from ast import arg


def area(x, y, z):
    print((((1/2) * (x + y + z))*(((1/2) * (x + y + z)) - x) * (((1/2) * (x + y + z)) - y) * (((1/2) * (x + y + z)) - z)) ** (1/2))
    

print(area(7, 4, 6))