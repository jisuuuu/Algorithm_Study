# Tri-du
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
print(a if a == b else max(a, b))