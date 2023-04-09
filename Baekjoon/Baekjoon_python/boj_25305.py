#커트라인
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
grades = list(map(int, sys.stdin.readline().rstrip().split()))
grades.sort(reverse=True)

print(grades[k - 1])