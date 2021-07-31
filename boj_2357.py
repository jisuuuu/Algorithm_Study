#최솟값과 최댓값
import sys
from math import *


#세그먼트 트리 초기화
def init_min(node, start, end):
    if start == end:
        tree_min[node] = nums[start]
        return tree_min[node]
    mid = (start + end) // 2
    tree_min[node] = min(init_min(node * 2, start, mid), init_min(node * 2 + 1, mid + 1, end))
    return tree_min[node]


def init_max(node, start, end):
    if start == end:
        tree_max[node] = nums[start]
        return tree_max[node]
    mid = (start + end) // 2
    tree_max[node] = max(init_max(node * 2, start, mid), init_max(node * 2 + 1, mid + 1, end))
    return tree_max[node]


def query_min(node, start, end, left, right):
    if start > right or end < left:
        return 1000000001
    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(query_min(node * 2, start, mid, left, right), query_min(node * 2 + 1, mid + 1, end, left, right))


def query_max(node, start, end, left , right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree_max[node]

    mid = (start + end) // 2
    return max(query_max(node * 2, start, mid, left, right), query_max(node * 2 + 1, mid + 1, end,left, right))


#main
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

#세그먼트 트리 사이즈 계산
h = int(ceil(log2(n)))
t_size = 1 << (h + 1)

tree_min = [0] * t_size
tree_max = [0] * t_size

init_min(1, 0, n - 1)
init_max(1, 0, n - 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(query_min(1, 0, n - 1, a - 1, b - 1), end=' ')
    print(query_max(1, 0, n - 1, a - 1, b - 1))

#시간 초과
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     new = nums[a - 1 : b]
#     print(f'{min(new)} {max(new)}')