#이게 분수?
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
c, d = map(int, sys.stdin.readline().rstrip().split())

example = list()
example.append(a / c + b / d)
example.append(c / d + a / b)
example.append(d / b + c / a)
example.append(b / a + d / c)
print(example.index(max(example)))