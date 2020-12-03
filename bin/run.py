#!/usr/bin/env python
import sys
from functools import reduce
from re import compile

from aoc2020 import *

if sys.argv[1] == "01.01":
    with open('res/01.txt', 'r') as f:
        f.seek(0)
        res = summands(2020, [int(line) for line in f], n=2)
        if res:
            print(reduce(int.__mul__, res, 1))
elif sys.argv[1] == "01.02":
    with open('res/01.txt', 'r') as f:
        f.seek(0)
        res = summands(2020, [int(line) for line in f], n=3)
        if res:
            print(reduce(int.__mul__, res, 1))
elif sys.argv[1] == "02.01":
    with open('res/02.txt', 'r') as f:
        print(passcheck([l for l in f]))
elif sys.argv[1] == "02.02":
    with open('res/02.txt', 'r') as f:
        print(passcheck2([l for l in f]))
elif sys.argv[1] == "03.01":
    with open('res/03.txt', 'r') as f:
        print(trajectory([l for l in f]))
