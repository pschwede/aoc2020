#!/usr/bin/env python

from re import compile

from lib.passcheck import passcheck

PATTERN = compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<what>\w): (?P<pass>\w+)")

with open('res/02.txt', 'r') as f:
    print(passcheck([l for l in f]))
