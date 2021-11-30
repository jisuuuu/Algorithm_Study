# Grading Exams
import sys
t = int(sys.stdin.readline().rstrip())

for k in range(t):
    n = int(sys.stdin.readline().rstrip())
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    cnt = 0

    for i in range(n):
        if a[i] != b[i]:
            cnt += 1
    print(f'Case {k + 1}: {cnt}')