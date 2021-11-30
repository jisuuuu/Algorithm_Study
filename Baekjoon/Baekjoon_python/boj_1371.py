#가장 많은 글자
import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = {}
word = sys.stdin.read()

for a in alphabet:
    result[a] = word.count(a)

items = sorted(result.items(), key=lambda x: (-x[1], x[0]))

max_count = items[0][1]
answer = ''
for i in items:
    if i[1] == max_count:
        answer += i[0]
print(answer)