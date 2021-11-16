#!/usr/bin/env python3
from packaging import version
import sys


def compare_versions(arg1, arg2):
    if version.parse(arg1) > version.parse(arg2):
        return 1
    elif version.parse(arg1) < version.parse(arg2):
        return -1
    else:
        return 0


print(compare_versions(sys.argv[1], sys.argv[2]))
