#자전거 속도
import sys
from math import pi

i = 1
while True:
    r, n, t = map(float, sys.stdin.readline().rstrip().split())
    if n == 0:
        break

    distance = r / 63360  * pi * n
    mph = distance / t * 3600
    print("Trip #%d: %.2f %.2f" % (i, distance, mph))
    i += 1