#!/usr/bin/env python
from typing import List

def summands(sum_: int, xs: List[int], n: int=1) -> int:
    """Find n summands in xs for some sum_"""
    if n<=1:
        return [sum_] if sum_ in xs else None
    for i, x in enumerate(xs):
        if n>0:
            res = summands(sum_ - x, xs[i+1:], n-1)
            if res:
                return [x] + res
