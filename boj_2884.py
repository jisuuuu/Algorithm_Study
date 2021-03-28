#알람 시계
import sys
h, m = map(int, sys.stdin.readline().rstrip().split())

if h > 0:
    if m < 45:
        print(f'{h - 1} {m + 60 - 45}')
    else:
        print(f'{h} {m - 45}')
else:
    if m < 45:
        print(f'23 {m + 60 - 45}')
    else:
        print(f'0 {m - 45}')