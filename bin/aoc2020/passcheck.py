#!/usr/bin/env python
from typing import List
from re import compile

PATTERN = compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<what>\w): (?P<pass>\w+)")

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
