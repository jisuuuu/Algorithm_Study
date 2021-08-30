#!/bin/python3

import os

def circularArrayRotation(a, k, queries):
    result = [0 for _ in range(len(a))]

    for i in range(len(a)):
        if i + k >= len(a):
            result[(i + k) % len(a)] = a[i]
        else:
            result[i + k] = a[i]

    new = []
    for q in queries:
        new.append(result[q])
    return new


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
