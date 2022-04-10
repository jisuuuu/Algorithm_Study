#Report Card Time
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    name, score = sys.stdin.readline().rstrip().split()
    real_score = int(score)

    if 97 <= real_score <= 100:
        print(name, 'A+')
    elif 90 <= real_score <= 96:
        print(name, 'A')
    elif 87 <= real_score <= 89:
        print(name, 'B+')
    elif 80 <= real_score <= 86:
        print(name, 'B')
    elif 77 <= real_score <= 79:
        print(name, 'C+')
    elif 70 <= real_score <= 76:
        print(name, 'C')
    elif 67 <= real_score <= 69:
        print(name, 'D+')
    elif 60 <= real_score <= 66:
        print(name, 'D')
    elif 0 <= real_score <= 59:
        print(name, 'F')