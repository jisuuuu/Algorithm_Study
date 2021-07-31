#시리얼 번호
import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    cnt = 0

    for w in word:
        if w.isdigit():
            cnt += int(w)
    arr.append((word, cnt))
arr.sort(key=lambda x : (len(x[0]), x[1], x[0])) #1. 길이 2. 숫자인 것 자리수 합 3. 사전순
for i in range(n):
    print(arr[i][0])
