#세금
import sys
n = int(sys.stdin.readline().rstrip())
print(int(n * 0.78), int(n * 0.8) + int(n * 0.2 * 0.78))