#애너그램 만들기
import sys
arr = [0 for _ in range(26)]

for i in list(sys.stdin.readline().rstrip()):
    arr[ord(i) - 97] += 1

for j in list(sys.stdin.readline().rstrip()):
    arr[ord(j) - 97] -= 1

print(sum(map(abs, arr)))