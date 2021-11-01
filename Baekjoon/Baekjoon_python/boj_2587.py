#대표값2
import sys
arr = []

for _ in range(5):
    arr.append(int(sys.stdin.readline().rstrip()))
print(sum(arr) // 5)
arr.sort()
print(arr[2])