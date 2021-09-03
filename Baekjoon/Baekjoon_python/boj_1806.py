#부분합

import sys
#시간초과 답 (완전 탐색)
# n, s = map(int, sys.stdin.readline().rstrip().split())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
# res = sys.maxsize
#
# for i in range(len(arr)):
#     idx = i
#     cnt = 0
#     total = 0
#     while total < s:
#         if idx >= len(arr):
#              break
#         total += arr[idx]
#         idx += 1
#         cnt += 1
#     if total == s:
#         if res > cnt:
#             res = cnt
# print(res)

n, s = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

start, end, tot = 0, 0, 0
min_length = sys.maxsize

while True:
    if tot >= s:
        min_length = min(min_length, end - start)
        tot -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        tot += arr[end]
        end += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)