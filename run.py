#!/usr/bin/env python
import sys
from functools import reduce
from re import compile

from aoc2020 import *

if sys.argv[1] == "01.01":
    with open('res/01.txt', 'r') as f:
        res = summands(2020, [int(line) for line in f], n=2)
        if res:
            print(reduce(int.__mul__, res, 1))
elif sys.argv[1] == "01.02":
    with open('res/01.txt', 'r') as f:
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
        print(trajectory(slope=(3, 1), lines=[l for l in f]))
elif sys.argv[1] == "03.02":
    with open('res/03.txt', 'r') as f:
        res=1
        for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
            f.seek(0)
            res *= trajectory(slope=slope, lines=[l for l in f])
        print(res)
