#두 용액
#두 개의 합이 가장 작은 것이므로 정렬 후 start, end 양 끝에서 시작한 후 줄여가며
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

start, end = 0, n - 1
result = []
answer = sys.maxsize

while start < end:
    total = arr[start] + arr[end]

    if abs(total) < answer:
        answer = abs(total)
        result = [arr[start], arr[end]]

    if total < 0:
        start += 1
    else:
        end -= 1
print(result[0], result[1])