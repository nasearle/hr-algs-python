#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# a is array to be rotated, d is number of left rotations
def rotLeft(a, d):
    # lenArr = len(a)
    # return a[d:lenArr] + a[:d]
    lenArr = len(a)
    newArr = [0] * lenArr
    for idx, elem in enumerate(a):
        newPos = (idx + (lenArr - d)) % lenArr
        newArr[newPos] = elem
    return newArr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()