#회사에 있는 사람
import sys
n = int(sys.stdin.readline().rstrip())
people = []

for _ in range(n):
    name, action = sys.stdin.readline().rstrip().split(' ')

    if action == 'enter':
        people.append(name)
    elif action == 'leave':
        people.remove(name)

print(' '.join(sorted(people, reverse=True)))