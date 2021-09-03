import sys
n = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
dp = [0 for _ in range(max(arr))]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2

for i in range(5, max(arr)):
    dp[i] = dp[i - 1] + dp[i - 5]

for a in arr:
    print(dp[a - 1])