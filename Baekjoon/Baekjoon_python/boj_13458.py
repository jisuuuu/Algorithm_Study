# 시험 감독
import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

cnt = N # 총 감독관은 무조건 한 명 필요하기 때문에

for a in A:
    if a >= B: # 총 감독관이 관리할 수 있는 수보다 작을 경우는 총 감독관만 필요하므로
        if (a - B) % C == 0:
            cnt += (a - B) // C
        else:
            cnt += (a - B) // C + 1

print(cnt)