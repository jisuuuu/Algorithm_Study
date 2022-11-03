#나누기
import sys
n = sys.stdin.readline().rstrip()
f = int(sys.stdin.readline().rstrip())

temp = int(n[:-2] + '00')

while True:
    if temp % f == 0:
        break
    temp += 1
print(str(temp)[-2:])