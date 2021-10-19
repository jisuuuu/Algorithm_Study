#첼시를 도와줘!
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    p = int(sys.stdin.readline().rstrip())

    price, name = 0, ''
    for _ in range(p):
        p, n = sys.stdin.readline().rstrip().split()
        p = int(p)

        if price < p:
            price = p
            name = n
    print(name)