#지능형 기차
import sys
max_num = -sys.maxsize
total = 0
for _ in range(4):
    minus, plus = map(int, sys.stdin.readline().rstrip().split())

    total = total - minus + plus

    if max_num < total:
        max_num = total
print(max_num)