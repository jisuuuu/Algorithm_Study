#JOI와 IOI
import sys
string = sys.stdin.readline()
joi_cnt = 0
ioi_cnt = 0

for i in range(len(string) - 2):
    if string[i:i + 3] == 'JOI':
        joi_cnt += 1
    elif string[i:i + 3] == 'IOI':
        ioi_cnt += 1

print(joi_cnt)
print(ioi_cnt)