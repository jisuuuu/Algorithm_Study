#경기 결과
import sys
n = int(sys.stdin.readline().rstrip())
result_a, result_b = 0, 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a < b:
        result_b += 1
    elif a > b:
        result_a += 1

print(result_a, result_b)