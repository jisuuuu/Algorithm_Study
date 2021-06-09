#알파벳 개수
import sys

st = sys.stdin.readline().rstrip()
arr = [chr(i) for i in range(97, 123)]
alpha = {arr[i] : 0 for i in range(len(arr))}

for s in st:
    alpha[s] += 1
arr = list(map(str, alpha.values()))
print(' '.join(arr))