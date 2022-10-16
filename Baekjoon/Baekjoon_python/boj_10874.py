#이교수님의 시험
import sys
n = int(sys.stdin.readline().rstrip())
answer = [(i - 1) % 5 + 1 for i in range(1, 11)]

for j in range(1, n + 1):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    if arr == answer:
        print(j)