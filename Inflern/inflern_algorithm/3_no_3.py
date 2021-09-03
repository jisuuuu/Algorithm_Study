#카드 역배치(정올 기출)
import sys
# sys.stdin = open("input.txt", "rt")
arr = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        arr[s + i], arr[e - i] = arr[e - i], arr[s + i]
print(' '.join(list(map(str, arr[1:]))))