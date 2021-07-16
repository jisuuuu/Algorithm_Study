#대표값
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))
# avg = round(sum(arr) / len(arr)) #round_half_even 방식이니 사용하지마
avg = int(sum(arr) / len(arr) + 0.5) #평균구하는 방식
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

#round_half_even 정확한 하프지점이 없으면 짝수쪽으로 가버림
print(round(4.500))
print(round(4.511))