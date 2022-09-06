#팀 이름 정하기
import sys
yeondo_name = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
team_name = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
max_num = 0
max_idx = 0

for i in range(n):

    l = yeondo_name.count('L') + team_name[i].count('L')
    o = yeondo_name.count('O') + team_name[i].count('O')
    v = yeondo_name.count('V') + team_name[i].count('V')
    e = yeondo_name.count('E') + team_name[i].count('E')

    result = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100

    if max_num < result:
        max_num = result
        max_idx = i
print(team_name[max_idx])