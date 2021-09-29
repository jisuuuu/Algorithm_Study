#Yangjojang of The Year
import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    school = ''
    alcohol = 0
    for _ in range(n):
        s, a = sys.stdin.readline().rstrip().split()

        if alcohol < int(a):
            alcohol = int(a)
            school = s
    print(school)
