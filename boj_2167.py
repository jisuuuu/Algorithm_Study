#2차원 배열의 합
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        dp[i][j] = matrix[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][ j - 1])