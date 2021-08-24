#막대기
import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
stack = 0
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
for i in range(len(arr) - 1, -1, -1):
    if stack < arr[i]:
        stack = arr[i]
        cnt += 1

print(cnt)