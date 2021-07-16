#대표값
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))
avg = round(sum(arr) / len(arr))
min_num = -1
min_point = float('inf')
idx = -1

for i, a in enumerate(arr):
    if abs(avg - a) < min_point:
        min_point = abs(avg - a)
        min_num = a
        idx = i
    elif abs(avg - a) == min_point:
        if min_num < a:
            min_num = a
            idx = i
print(f'{avg} {idx + 1}')