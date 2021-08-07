#하얀 칸
import sys
chess = [list(sys.stdin.readline().rstrip()) for _ in range(8)]
cnt = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                if chess[i][j] == 'F':
                    cnt += 1
    else:
        for j in range(8):
            if j % 2 == 1:
                if chess[i][j] == 'F':
                    cnt += 1
print(cnt)