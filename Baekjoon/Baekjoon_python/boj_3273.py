#두 수의 합
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())
left, right = 0, n - 1
answer = 0

arr.sort()

while left < right:
    tmp = arr[left] + arr[right]

    if tmp == x:
        answer += 1
    elif tmp < x:
        left += 1
        continue
    right -= 1
print(answer)