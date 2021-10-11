#내 학점을 구해줘
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    total, grade = 0, 0

    for _ in range(n):
        c, g = map(float, sys.stdin.readline().rstrip().split())
        total += c
        grade += c * g
    gpa = grade / total
    print(int(total), '%.1f' %gpa)