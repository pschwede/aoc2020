#!/usr/bin/env python
from functools import reduce

from lib.summands import summands

if __name__ == "__main__":
    with open('res/01.txt', 'r') as f:
        f.seek(0)
        res = summands(2020, [int(line) for line in f], n=3)
        if res:
            print(reduce(int.__mul__, res, 1))
