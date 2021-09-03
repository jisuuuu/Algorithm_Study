#동전 1
#dp로 풀기
#dp[n] = dp[n] + dp[n - k] (if n - k >= 0)
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coin = []
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

for c in coin:
    for i in range(1, k + 1):
        if i - c >= 0:
            dp[i] += dp[i - c]
print(dp[k])