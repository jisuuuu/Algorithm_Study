#카드 뽑기
import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
print(min(m, k) + min(n - m, n - k))