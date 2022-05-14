#Boiling Water
import sys
b = int(sys.stdin.readline().rstrip())
print(b * 5 - 400)

if b > 100:
    print(-1)
elif b < 100:
    print(1)
else:
    print(0)