# 스타트와 링크
import sys, itertools
n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cases = list(itertools.combinations([i for i in range(n)], int(n / 2)))

min_num = sys.maxsize

for case_a in cases:
    start_team = 0
    link_team = 0

    for x in case_a:
        for y in case_a:
            start_team += arr[x][y]

    case_b = [i for i in range(n) if i not in case_a]
    for x in case_b:
        for y in case_b:
            link_team += arr[x][y]

    min_num = min(min_num, abs(start_team - link_team))
print(min_num)