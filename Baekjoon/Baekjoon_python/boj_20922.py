#겹치는 건 싫어
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
left, right = 0, 0
answer = 0
count = [0] * (max(arr) + 1)

while right < n:
    if count[arr[right]] < k:
        count[arr[right]] += 1
        right += 1
    else:
        count[arr[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)
