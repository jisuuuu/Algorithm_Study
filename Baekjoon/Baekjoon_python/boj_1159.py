#농구 경기
import sys
n = int(sys.stdin.readline().rstrip())
members = dict()

for _ in range(n):
    name = sys.stdin.readline().rstrip()

    if name[0] in members.keys():
        members[name[0]] += 1
    else:
        members[name[0]] = 1

result = []

for k, v in members.items():
    if v >= 5:
        result.append(k)

if not result:
    print('PREDAJA')
else:
    print(''.join(sorted(result)))