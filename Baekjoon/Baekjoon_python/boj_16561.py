#3의 배수
import sys
n = int(sys.stdin.readline().rstrip())
answer = 1
cnt = 2

for i in range(9, n, 3):
    answer = answer + cnt
    cnt += 1
print(answer)