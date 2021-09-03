#세로 읽기
import sys
words = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
# print(words)
# print(max([len(words[i]) for i in range(5)]))
max_len = max([len(words[i]) for i in range(5)])
answer = ''
for i in range(max_len):
    for j in range(5):
        if len(words[j]) <= i:
            continue
        else:
            answer += words[j][i]
print(answer)