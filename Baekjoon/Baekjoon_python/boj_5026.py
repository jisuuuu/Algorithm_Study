#박사 과정
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    result = sys.stdin.readline().rstrip()

    if result == 'P=NP':
        print('skipped')
    else:
        a, b = map(int, result.split('+'))
        print(a + b)