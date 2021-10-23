#결혼식
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
friends = dict()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a in friends:
        friends[a].append(b)
    else:
        friends[a] = [b]

    if b in friends:
        friends[b].append(a)
    else:
        friends[b] = [a]


def dfs(i, c):
    global friend

    if i != 1:
        friend.add(i)

    if c == 2:
        return

    for j in friends[i]:
        if not check[j]:
            check[j] = True
            dfs(j, c + 1)
            check[j] = False


check = [False for _ in range(n + 1)]
friend = set()

check[1] = True
if 1 in friends:
    dfs(1, 0)

print(len(friend))