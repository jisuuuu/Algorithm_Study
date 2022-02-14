#파일 옮기기
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
c, d = map(int, sys.stdin.readline().rstrip().split())

print(min(a + d, b + c))