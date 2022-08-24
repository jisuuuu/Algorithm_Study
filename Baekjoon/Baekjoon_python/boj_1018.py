#체스판 다시 칠하기
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
chess = []

for _ in range(n):
    chess.append(list(sys.stdin.readline().rstrip()))

repair = []
for i in range(n - 7):
    for j in range(m - 7): # 8*8으로 자를 때 index 오류를 해결하기 위해 -7
        w_index = 0 #흰색으로 시작
        b_index = 0 #검은색으로 시작

        for k in range(i, i + 8):
            for r in range(j, j + 8):
                if (k + r) % 2 == 0: #짝수인 경우
                    if chess[k][r] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else: #홀수인 경우
                    if chess[k][r] != 'B':
                        w_index += 1
                    else:
                        b_index += 1
        repair.append(w_index) #흰색으로 시작할 때 경우의 수
        repair.append(b_index) #검은색으로 시작할 때 경우의 수
print(min(repair))