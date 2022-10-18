# 해밍 거리
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    distance = 0
    num1 = sys.stdin.readline().rstrip()
    num2 = sys.stdin.readline().rstrip()

    for n1, n2 in zip(num1, num2):
        if n1 != n2:
            distance += 1
    print(f'Hamming distance is {distance}.')
