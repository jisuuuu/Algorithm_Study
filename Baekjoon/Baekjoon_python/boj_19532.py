#수학은 비대면강의입니다
import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split())

x = (c * e - b * f) // (a * e - b * d)
y = (c * d - a * f) // (b * d - a * e)

print(x, y)