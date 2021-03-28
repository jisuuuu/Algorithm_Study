# 단어 공부
import sys
word = list(sys.stdin.readline().rstrip().upper())
unique_word = list(set(word))

cnt_list = []
for w in unique_word:
    cnt = word.count(w)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(unique_word[cnt_list.index(max(cnt_list))])