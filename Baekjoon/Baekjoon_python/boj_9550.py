#아이들은 사탕을 좋아해
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    candies = list(map(int, sys.stdin.readline().rstrip().split()))

    answer = 0

    for c in candies:
        answer += c // k
    print(answer)