#전자레인지
import sys
temp = []
for _ in range(5):
    temp.append(int(sys.stdin.readline().rstrip()))

time = 0
if temp[0] < 0:
    time += (abs(temp[0]) * temp[2])
    time += temp[3]
    time += temp[1] * temp[4]
else:
    time += (temp[1] - temp[0]) * temp[4]
print(time)