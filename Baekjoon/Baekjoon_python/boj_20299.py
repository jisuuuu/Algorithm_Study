#3대 측정
import sys
n, k, l = map(int, sys.stdin.readline().rstrip().split())
answer = []
cnt = 0

for _ in range(n):
    team = list(map(int, sys.stdin.readline().rstrip().split()))

    is_pass = True
    for t in team:
        if t < l:
            is_pass = False
            break
    if is_pass:
        if sum(team) >= k:
            answer.extend(team)
            cnt += 1

print(cnt)
print(*answer)