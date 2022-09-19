#Gauß
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    result = (b - a + 1) * (a + b) // 2

    print(f'Scenario #{i}:')
    print(result)
    print()