#연속구간
import sys
for _ in range(3):
    arr = list(map(int, list(sys.stdin.readline().rstrip())))

    max_cnt = 1
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            cnt += 1
        else:
            cnt = 1

        if cnt > max_cnt:
            max_cnt = cnt
    print(max_cnt)