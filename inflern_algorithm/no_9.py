#주사위 게임
# def dice(arr):
#     new = set(arr)
#
#     if len(new) == 3:
#         return max(arr) * 100
#     elif len(new) == 2:
#         for i, n in enumerate(new):
#             if arr[i] != n:
#                 return n * 100 + 1000
#     else:
#         return arr[0] * 1000 + 10000
#
#
import sys
# #sys.stdin = open("input.txt", "rt")
# n = int(input())
# max_num = 0
# for _ in range(n):
#     arr = list(map(int, input().split()))
#     res = dice(arr)
#
#     if max_num < res:
#         max_num = res
# print(max_num)

# sys.stdin = open("input.txt", "rt")
n = int(input())
res = 0

for _ in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100

    if money > res:
        res = money
print(res)