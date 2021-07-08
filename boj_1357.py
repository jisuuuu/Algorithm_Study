#뒤집힌 덧셈
import sys
x, y = sys.stdin.readline().rstrip().split()
print(int(str(int(x[::-1]) + int(y[::-1]))[::-1]))