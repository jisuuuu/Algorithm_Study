#8진수
import sys
number = sys.stdin.readline().rstrip()
print(oct(int('0b' + number, 2)).lstrip('0o'))