#방학 숙제
import sys
l = int(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())

math = b // d if (b % d) == 0 else b // d + 1
korean = a // c if (a % c) == 0 else a // c + 1

if math > korean:
    print(l - math)
else:
    print(l - korean)