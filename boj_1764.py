#듣보잡
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
n_arr, m_arr = [], []

for _ in range(n):
    n_arr.append(sys.stdin.readline().rstrip())
for _ in range(m):
    m_arr.append(sys.stdin.readline().rstrip())
ans = list(sorted(set(n_arr) & set(m_arr)))
print(len(ans))
for a in ans:
    print(a)
