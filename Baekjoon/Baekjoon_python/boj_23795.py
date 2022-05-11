#사장님 도박은 재미로 하셔야 합니다
import sys
total = 0

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == -1:
        break

    total += n
print(total)