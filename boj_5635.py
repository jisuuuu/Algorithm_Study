#생일
import sys

n = int(sys.stdin.readline().rstrip())
students = []

for _ in range(n):
    s = list(sys.stdin.readline().rstrip().split())
    students.append({'name' : s[0], 'year' : int(s[3]), 'month' : int(s[2]), 'day' : int(s[1])})
new_s = sorted(students, key=lambda x : (-x['year'], -x['month'], -x['day']))
print(new_s[0]['name'])
print(new_s[len(students) - 1]['name'])