#땅따먹기
def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(len(land))]

    #dp 맨 아래 land 값 넣음
    dp[len(land) - 1][0] = land[len(land) - 1][0]
    dp[len(land) - 1][1] = land[len(land) - 1][1]
    dp[len(land) - 1][2] = land[len(land) - 1][2]
    dp[len(land) - 1][3] = land[len(land) - 1][3]

    #for문 돌면서 현재 idx 뺀 값 중 가장 큰 값 저장
    for i in range(len(land) - 2, -1, -1):
        dp[i][0] = land[i][0] + max(dp[i + 1][1], max(dp[i + 1][2], dp[i + 1][3]))
        dp[i][1] = land[i][1] + max(dp[i + 1][0], max(dp[i + 1][2], dp[i + 1][3]))
        dp[i][2] = land[i][2] + max(dp[i + 1][1], max(dp[i + 1][0], dp[i + 1][3]))
        dp[i][3] = land[i][3] + max(dp[i + 1][1], max(dp[i + 1][2], dp[i + 1][0]))

    return max(dp[0])