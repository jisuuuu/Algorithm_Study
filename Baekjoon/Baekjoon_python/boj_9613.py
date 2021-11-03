#GCD 합
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    n = arr.pop(0)

    total = 0

    for i in range(n):
        for j in range(n):
            if i < j:
                total += gcd(arr[i], arr[j])

    print(total)