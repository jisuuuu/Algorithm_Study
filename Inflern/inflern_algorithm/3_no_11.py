#격자판 회문수
import sys


def check(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True


sys.stdin = open("input.txt", "rt")
result = 0
cnt = 0
matrix = [list(map(int, input().split())) for _ in range(7)]


for i in range(7):
    for j in range(3):
        ch1 = [0] * 5
        ch2 = [0] * 5
        for k in range(5):
            ch1[k] = matrix[j + k][i]
            ch2[k] = matrix[i][j + k]

            if check(ch1):
                result += 1
            if check(ch2):
                result += 1

for i in range(3):
    for j in range(7):
        tmp = matrix[j][i : i + 5]

        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):
            if matrix[i + k][j] != matrix[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)
print(result)