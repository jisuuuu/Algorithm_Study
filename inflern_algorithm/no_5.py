#정다면체
import sys
# sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
cnt = [0 for _ in range(n + m + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

max_num = max(cnt)
for i, c in enumerate(cnt):
    if c == max_num:
        print(i, end=' ')