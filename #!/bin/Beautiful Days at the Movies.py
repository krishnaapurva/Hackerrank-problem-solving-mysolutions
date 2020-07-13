#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    cnt = 0
    for m in range(i,j+1):
        cn = str(m)
        rev = int(cn[::-1])
        diff = abs(rev-m)
        if((diff%k)==0):
            cnt = cnt+1
    return(cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
