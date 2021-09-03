#!/bin/python3

import os


def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    check, cnt = 0, 0

    for i in range(n - 1):
        if check == 1:
            check = 0
            continue
        if ar[i] == ar[i + 1]:
            cnt += 1
            check = 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
