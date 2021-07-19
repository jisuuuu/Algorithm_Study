#자릿수의 합
import sys


def digit_sum(x):
    total = 0
    for a in str(x):
        total += int(a) # 좀 더 파이썬 같은 코드(내가 짬)

    # while x > 0:
    #     total += x % 10
    #     x = x // 10

    return total


# sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))
max_num = -sys.maxsize
idx = -1
for i, a in enumerate(arr):
    num = digit_sum(a)
    if num > max_num:
        max_num = num
        idx = i
print(arr[idx])