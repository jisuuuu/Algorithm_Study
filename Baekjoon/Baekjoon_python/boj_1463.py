#1로 만들기
import sys
n = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1): # 2부터 n까지 반복
    dp[i] = dp[i - 1] + 1 # 1을 빼는 연산 -> 1회 진행

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1) # 2로 나누어 떨어질 때, 2로 나누는 연산
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1) # 3으로 나누어 떨어질 때, 3으로 나누는 연산

print(dp[n])