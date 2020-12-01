#!/usr/bin/env python
from functools import reduce
from typing import List

"""Find two summands """
def summands(sum_: int, xs: List[int], n: int=1) -> int:
    if n==1:
        return [sum_] if sum_ in xs else None
    for i, x in enumerate(xs):
        if n>0:
            res = summands(sum_ - x, xs[i+1:], n-1)
            if res:
                return [x] + res

if __name__ == "__main__":
    with open('res/01.txt', 'r') as f:
        for n in range(1,4):
            f.seek(0)
            smmds = summands(2020, [int(line) for line in f], n=n)
            if smmds:
                print(n, reduce(int.__mul__, smmds, 1))
