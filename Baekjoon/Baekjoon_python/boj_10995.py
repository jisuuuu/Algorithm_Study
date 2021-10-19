#별 찍기 - 20
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    result = '*'
    for j in range(n - 1):
        result += ' *'

    if i % 2 == 0:
        print(' ' + result)
    else:
        print(result)