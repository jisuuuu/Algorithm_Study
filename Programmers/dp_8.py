#2XN 타일링
#피보나치
def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007 #제한사항 확인하기 1,000,000,007 나눈 나머지라고 명시함
    return dp[n]