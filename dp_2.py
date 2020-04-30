#타일장식물
def solution(N):
    dp = [0 for i in range(0, N)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N):
        dp[i] = dp[i - 1] + dp[i - 2]

    return 2 * (dp[N - 1] + dp[N - 2] + dp[N - 2] + dp[N - 3])