#!/usr/bin/env python3
import sys


def comparison(v):
    return tuple(map(int, (v.split("."))))


if comparison(sys.argv[1]) > comparison(sys.argv[2]):
    print(1)
elif comparison(sys.argv[1]) < comparison(sys.argv[2]):
    print(-1)
else:
    print(0)
