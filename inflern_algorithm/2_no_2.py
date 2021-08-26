#K번째 수
import sys
#sys.stdin = open("input.txt", "rt")
t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    new = sorted(arr[s - 1:e])
    print(f'#{i + 1} {new[k - 1]}')