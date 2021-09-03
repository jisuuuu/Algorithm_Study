#제로
import sys

k = int(sys.stdin.readline().rstrip())
q = list()
for _ in range(k):
    n = int(sys.stdin.readline().rstrip())

    if n == 0 and len(q) != 0:
        q.pop()
        continue
    q.append(n)
print(sum(q))