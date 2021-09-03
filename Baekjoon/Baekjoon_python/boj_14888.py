#연산자 끼워넣기

import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
add, sub, mul, div = map(int, sys.stdin.readline().rstrip().split())

max_num = -sys.maxsize - 1 #100000은 에러가 발생 10억보다 크다는 조건에 걸린듯
min_num = sys.maxsize


def dfs(i, res, add, sub, mul, div):
    global max_num, min_num
    if i == n:
        max_num = max(res, max_num)
        min_num = min(res, min_num)
        return

    if add:
        dfs(i + 1, res + num[i], add - 1, sub, mul, div)
    if sub:
        dfs(i + 1, res - num[i], add, sub - 1, mul, div)
    if mul:
        dfs(i + 1, res * num[i], add, sub, mul - 1, div)
    if div:
        dfs(i + 1, int(res / num[i]), add, sub, mul, div - 1)


dfs(1, num[0], add, sub, mul, div)
print(max_num)
print(min_num)