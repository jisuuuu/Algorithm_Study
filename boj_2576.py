#홀수
import sys
odd_min = sys.maxsize
odd_sum = 0
for _ in range(7):
    n = int(sys.stdin.readline().rstrip())

    if n % 2 != 0:
        odd_sum += n

        if odd_min > n:
            odd_min = n
if odd_sum != 0:
    print(odd_sum)
    print(odd_min)
else:
    print(-1)