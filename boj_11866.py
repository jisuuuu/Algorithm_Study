#요세푸스 문제 0
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
queue = [i for i in range(1, n + 1)]
answer = []
idx = 0

while queue:
    idx += k - 1
    if idx > len(queue) - 1:
        idx %= len(queue)
    answer.append(queue.pop(idx))
print('<' + str(answer)[1:-1] + '>')