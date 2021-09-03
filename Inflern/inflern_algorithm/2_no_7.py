#소수(에라토스테네스 체)
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
prime = [False for _ in range(n + 1)]
cnt = 0
for i in range(2, n + 1):
    if not prime[i]:
        cnt += 1
        for j in range(i + i, n + 1, i):
            prime[j] = True
print(cnt)
print([i for i in range(2, n) if prime[i] == False])