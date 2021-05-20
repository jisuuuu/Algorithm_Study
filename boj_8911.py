#거북이
import sys
t = int(sys.stdin.readline().rstrip())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(t):
    move = list(sys.stdin.readline().rstrip())
    px = 0
    py = 0
    pd = 0 #북 0 서 1 남 2 북 3
    trace = [(px, py)]

    for m in move:
        if m == 'F':
            px = px + dx[pd]
            py = py + dy[pd]
        elif m == 'B':
            px = px - dx[pd]
            py = py - dy[pd]
        elif m == 'L':
            if pd == 3:
                pd = 0
            else:
                pd = pd + 1
        elif m == 'R':
            if pd == 0:
                pd = 3
            else:
                pd = pd - 1

        trace.append((px, py))

    width = max(trace, key = lambda x:x[0])[0] - min(trace, key = lambda x:x[0])[0]
    heigth = max(trace, key = lambda x:x[1])[1] - min(trace, key = lambda x:x[1])[1]
    print(width * heigth)
