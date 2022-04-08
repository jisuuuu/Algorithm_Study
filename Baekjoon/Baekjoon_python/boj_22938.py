#백발백준하는 명사수
import sys
x_1, y_1, r_1 = map(int, sys.stdin.readline().rstrip().split())
x_2, y_2, r_2 = map(int, sys.stdin.readline().rstrip().split())

d = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
print('YES' if (r_1 + r_2) ** 2 > d else 'NO')