#기타리스트

import sys

n, s, m = map(int, sys.stdin.readline().rstrip().split())
v = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j]:
            if j + v[i] <= m:
                dp[i + 1][j + v[i]] = 1
            if j - v[i] >= 0:
                dp[i + 1][j - v[i]] = 1

answer = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        answer = i
        break
print(answer)