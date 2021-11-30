#Ahmed Aly
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    cases = sys.stdin.readline().rstrip().split()

    if cases[1] == '+':
        result = int(cases[0]) + int(cases[2])
    else:
        result = int(cases[0]) - int(cases[2])

    if result == int(cases[4]):
        print(f'Case {i}: YES')
    else:
        print(f'Case {i}: NO')