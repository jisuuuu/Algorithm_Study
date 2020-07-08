#올림픽
import sys
answer = 1 #(자신보다 더 잘한 나라 수) + 1 이기 때문에 1로 초기화
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
idx = -1
for i in range(N):
    if arr[i][0] == K:
        idx = i

for i in range(N):
    if arr[i][1] > arr[idx][1]:
        answer += 1
    elif arr[i][1] == arr[idx][1]:
        if arr[i][2] > arr[idx][2]:
            answer += 1
        elif arr[i][2] == arr[idx][2]:
            if arr[i][3] > arr[idx][3]:
                answer += 1

print(answer)