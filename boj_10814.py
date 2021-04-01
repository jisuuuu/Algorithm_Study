#나이순 정렬
import sys

n = int(sys.stdin.readline().rstrip())
members = []

for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    members.append((int(age), name))

members = sorted(members, key=lambda x:x[0])

for m in members:
    print(f'{m[0]} {m[1]}')