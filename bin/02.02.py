#!/usr/bin/env python

from re import compile

from lib.passcheck import passcheck2

PATTERN = compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<what>\w): (?P<pass>\w+)")

with open('res/02.txt', 'r') as f:
    print(passcheck2([l for l in f]))
