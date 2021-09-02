#봉우리
import sys
# sys.stdin = open("input.txt", "rt")
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

#0 초기화
arr.insert(0, [0] * n)
arr.append([0] * n)

for a in arr:
    a.insert(0, 0)
    a.append(0)

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        #내가 푼 풀이
        if arr[i][j] > max([arr[i - 1][j], arr[i + 1][j], arr[i][j - 1], arr[i][j + 1]]):
            cnt += 1
        #강사 풀이 all 이라는 함수 사용하면 깔끔하게 정리 가능
        # if all(arr[i][j] > arr[i + dx[k]][j + dy[k]] for k in range(4)):
        #     cnt += 1
print(cnt)