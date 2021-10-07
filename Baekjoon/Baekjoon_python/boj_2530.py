#인공지능 시계
import sys
h, m, s = map(int, sys.stdin.readline().rstrip().split())
d = int(sys.stdin.readline().rstrip())

s += d % 60
d = d // 60

if s >= 60:
    s -= 60
    m += 1

m += d % 60
d = d // 60

if m >= 60:
    m -= 60
    h += 1

h += d % 24
if h > 23:
    h -= 24

print(h, m, s)