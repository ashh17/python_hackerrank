#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    ct1 = 0
    ct2 = 0
    for x in apples:
        x += a
        if x in range(s, t+1):
            ct1 = ct1+1
    print(ct1)
    for y in oranges:
        y += b
        if y in range(s, t+1):
            ct2 = ct2+1
    print(ct2)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
