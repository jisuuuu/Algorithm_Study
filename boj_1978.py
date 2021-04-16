#소수 찾기
import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0

for n in nums:
    cnt = 0

    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    if cnt == 2:
        ans += 1

print(ans)