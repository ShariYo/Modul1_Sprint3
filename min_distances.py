#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def minimumDistances(a):
    # Write your code here
    results = []
    for first in range(len(a)):
        for second in range(first + 1, len(a)):
            if a[first] == a[second]:
                res = abs(first - second)
                results.append(res)
            else:
                pass

    return "-1" if not results else min(results)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + "\n")

    fptr.close()
