from typing import List
from re import compile

PATTERN = compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<what>\w): (?P<pass>\w+)")

def trajectory(lines: List[str]) -> int:
    trees = 0
    return trees

def passcheck(lines: List[str]) -> int:
    """counts valid passwords"""
    okay: int = 0
    for d in [PATTERN.match(line).groupdict() for line in lines]:
        if int(d['min']) <= d['pass'].count(d['what']) <= int(d['max']):
            okay += 1
    return okay


def passcheck2(lines: List[str]) -> int:
    """counts valid passwords"""
    okay: int = 0
    for d in [PATTERN.match(line).groupdict() for line in lines]:
        pos: int = int(d['min'])-1
        pos2: int = int(d['max'])-1
        try:
            if (d['pass'][pos]+d['pass'][pos2]).count(d['what']) == 1:
                print(d)
                okay += 1
        except IndexError:
            continue
    return okay


def summands(sum_: int, xs: List[int], n: int=1) -> int:
    """Find n summands in xs for some sum_"""
    if n<=1:
        return [sum_] if sum_ in xs else None
    for i, x in enumerate(xs):
        if n>0:
            res = summands(sum_ - x, xs[i+1:], n-1)
            if res:
                return [x] + res
