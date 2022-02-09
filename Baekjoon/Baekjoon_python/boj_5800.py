#성적 통계
import sys
k = int(sys.stdin.readline().rstrip())

for i in range(k):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    n = arr[0]
    scores = sorted(arr[1:], reverse=True)
    max_num = 0

    for j in range(1, len(scores)):
        if max_num < (scores[j - 1] - scores[j]):
            max_num = scores[j - 1] - scores[j]

    print(f'Class {i + 1}')
    print(f'Max {max(scores)}, Min {min(scores)}, Largest gap {max_num}')