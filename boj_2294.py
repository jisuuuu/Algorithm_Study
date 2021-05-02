#동전2
# dp
# D(i,k)
# {
#     [C(i) > k] D(i-1,k)
#     [C(i) = k] 1
#     [C(i) ≤ k] min(D(i-1,k),D(i,k-C(i)) + D(C(i)))
# }
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for c in coins:
    for j in range(1, k + 1):
        if c == j:
            dp[j] = 1
        elif c <= j:
            dp[j] = min(dp[j], (dp[c] + dp[j - c]))

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])