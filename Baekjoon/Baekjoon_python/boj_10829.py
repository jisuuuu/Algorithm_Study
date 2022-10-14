#이진수 변환
import sys
n = int(sys.stdin.readline().rstrip())
print(bin(n).lstrip('0b'))