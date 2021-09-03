# 사탕 게임
# 브루트 포스 (무식한 힘, 완전 탐색)
import sys


def check(a, s_row, e_row, s_col, e_col):
    n = len(a)
    result = 1

    #행 체크
    for i in range(s_row, e_row + 1):
        cnt = 1

        for j in range(1, n): #끝 쪽은 체크 안해도 똑같으니까
            if a[i][j - 1] == a[i][j]:
                cnt += 1
            else:
                cnt = 1

            if cnt > result:
                result = cnt

    #열 체크
    for i in range(s_col, e_col + 1):
        cnt = 1

        for j in range(1, n): #끝 쪽은 체크 안해도 똑같으니까
            if a[j - 1][i] == a[j][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > result:
                result = cnt

    return result


n = int(sys.stdin.readline().rstrip())
candy = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

result = 0

for i in range(n):
    for j in range(n):
        if j < n - 1:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            temp = check(candy, i, i, j, j + 1)

            if temp > result:
                result = temp

            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        if i < n - 1:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            temp = check(candy, i, i + 1, j, j)

            if temp > result:
                result = temp
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

print(result)