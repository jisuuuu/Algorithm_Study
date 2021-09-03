#심부름 가는 길
import sys
total = 0
for _ in range(4):
    total += int(sys.stdin.readline().rstrip())

print(total // 60)
print(total % 60)