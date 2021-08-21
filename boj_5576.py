#콘테스트
import sys
w = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
w.sort()
k = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
k.sort()
print(f'{sum(w[7:])} {sum(k[7:])}')