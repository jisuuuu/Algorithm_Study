#영수증
import sys
total = int(sys.stdin.readline().rstrip())
for _ in range(9):
    total -= int(sys.stdin.readline().rstrip())
print(total)