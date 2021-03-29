# 수 정렬하기
import sys

n = int(sys.stdin.readline().rstrip())
new = []

for _ in range(n):
    new.append(int(sys.stdin.readline().rstrip()))

new.sort()

for n in new:
    print(n)