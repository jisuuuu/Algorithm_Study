#숫자 카드
import sys
n = int(sys.stdin.readline().rstrip())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = {m_arr[i] : 0 for i in range(m)}

for i in range(n):
    if n_arr[i] in result.keys():
        result[n_arr[i]] += 1
print(" ".join(map(str, list(result.values()))))