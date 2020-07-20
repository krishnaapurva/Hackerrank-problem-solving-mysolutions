#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    li = []
    for i in range(d,d+n):
        x = i%n
        li.append(str(a[x]))
    print(' '.join(li))
