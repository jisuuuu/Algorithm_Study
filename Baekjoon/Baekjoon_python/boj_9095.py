#1, 2, 3 더하기
import sys
t = int(sys.stdin.readline().rstrip())
num = []
max_num = 0;
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    num.append(n)
    if max_num < n:
        max_num = n #입력을 받으면서 max를 확인해야 시간 초과 안됨

dp = [0 for _ in range(max_num + 1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_num + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for n in num:
    print(dp[n])