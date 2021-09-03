#전화번호 목록
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    calls = [sys.stdin.readline().rstrip() for _ in range(t)]
    calls.sort()

    for i in range(len(calls) - 1):
        if calls[i] in calls[i + 1][0 : len(calls[i])]:
            print('NO')
            break
    else:
        print('YES')