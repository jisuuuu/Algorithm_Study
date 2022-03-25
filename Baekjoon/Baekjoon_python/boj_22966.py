#가장 쉬운 문제를 찾는 문제
import sys
n = int(sys.stdin.readline().rstrip())
example = dict()

for _ in range(n):
    e, k = sys.stdin.readline().rstrip().split()
    example[e] = int(k)
print(sorted(example.items(), key=lambda x:x[1])[0][0])