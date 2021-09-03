#그룹 단어 체커

import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i] == word[i + 1]:
                pass
            elif word[i] in word[i + 1:]:
                break
        else:
            cnt += 1
print(cnt)