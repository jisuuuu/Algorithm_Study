#짝수를 찾아라
import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    tester = map(int, sys.stdin.readline().rstrip().split())

    total, smallest = 0, sys.maxsize

    for t in tester:
        if t % 2 == 0:
            total += t

            if smallest > t:
                smallest = t
    print(total, smallest)