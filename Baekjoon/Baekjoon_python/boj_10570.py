#Favorite Number
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    d = dict()

    for _ in range(m):
        num = int(sys.stdin.readline().rstrip())

        if num not in d.keys():
            d[num] = 1
        else:
            d[num] += 1
    print(sorted(d.items(), key=lambda x:(x[1], -x[0]), reverse=True)[0][0])