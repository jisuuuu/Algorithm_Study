#파일 완전 삭제
import sys
n = int(sys.stdin.readline().rstrip())
a, b = list(sys.stdin.readline().rstrip()), list(sys.stdin.readline().rstrip())

for _ in range(n):
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
        else:
            a[i] = '0'
print("Deletion succeeded" if a == b else "Deletion failed")