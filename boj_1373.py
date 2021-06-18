#2진수 8진수
import sys
two = '0b' + sys.stdin.readline().rstrip()
eight = oct(int(two, 2)).replace('0o', '')
print(eight)
