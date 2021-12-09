#FBI
import sys
result = []

for i in range(5):
    name = sys.stdin.readline().rstrip()

    if 'FBI' in name:
        result.append(i + 1)

if result:
    print(*result)
else:
    print('HE GOT AWAY!')