#소수 찾기
import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(m, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1

    if cnt == 2:
        arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1) #체크 안하니 오류