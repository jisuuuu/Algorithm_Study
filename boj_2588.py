# 곱셈
import sys

a = int(sys.stdin.readline().rstrip())
b_list = list(map(int, sys.stdin.readline().rstrip()))

sum = 0

for i in range(2, -1, -1):
    print(a * b_list[i])
    sum += a * b_list[i] * pow(10, 3 - i - 1)
print(sum)