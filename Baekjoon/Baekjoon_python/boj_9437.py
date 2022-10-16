#사라진 페이지 찾기
import sys
while True:
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    if numbers == [0]:
        break

    for i in range(numbers[0] // 4):
        arr = [2 * i + 1, 2 * i + 2, numbers[0] - 2 * i - 1, numbers[0] - 2 * i]

        if numbers[1] in arr:
            arr.remove(numbers[1])
            print(*arr)