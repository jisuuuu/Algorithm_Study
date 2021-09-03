#K번째 큰 수
import sys
#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = set()

#중복을 방지하기 위한 3중포문
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(arr[i] + arr[j] + arr[m])
res = list(res)
res.sort(reverse=True)
print(res[k - 1])