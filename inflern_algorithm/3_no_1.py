#희문 문자열 검사
import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
for j in range(n):
    word = input().lower()

    for i in range(len(word) // 2):
        if word[len(word) - i - 1] != word[i]:
            print(f'#{j + 1} NO')
            break
    else:
        print(f'#{j + 1} YES')