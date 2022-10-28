#Generations of Tribbles
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    dp = [1, 1, 2, 4]
    num = int(sys.stdin.readline().rstrip())

    for i in range(4, num + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4])
    print(dp[num])