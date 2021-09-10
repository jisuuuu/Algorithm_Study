#카드 역배치
import sys
arr = list(range(21))

for _ in range(10):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    for i in range((b - a + 1) // 2):
        arr[a + i], arr[b - i] = arr[b - i], arr[a + i]
print(' '.join(list(map(str, arr[1:]))))