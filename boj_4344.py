#평균은 넘겠지
import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    avg = sum(num[1:]) / num[0]
    cnt = 0

    for i in range(1, num[0] + 1):
        if avg < num[i]:
            cnt += 1

    print(f'{cnt / num[0] * 100:.3f}%')