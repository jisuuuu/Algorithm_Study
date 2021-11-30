#숫자의 개수 2
import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
count = [0 for _ in range(10)]
result = str(a * b * c)

for r in result:
    count[int(r)] += 1

for c in count:
    print(c)