#회의실 배정
import sys
n = int(sys.stdin.readline().rstrip())
arr = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0])) #1. 종료시간 기준으로 정렬 2. 시작시간 기준으로 정렬

ans = end = 0
for s, e in arr:
    if s >= end: #다음 시작점이 끝시간이랑 같은 것도 되니까 같거나 클 때
        ans += 1
        end = e
print(ans)