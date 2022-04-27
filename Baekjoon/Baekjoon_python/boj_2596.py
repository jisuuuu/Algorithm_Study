#비밀편지
import sys
change = {'000000': 'A', '001111': 'B', '010011': 'C', '011100': 'D'
    , '100110': 'E', '101001': 'F', '110101': 'G', '111010': 'H'}
n = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
result = ''
for i in range(0, n * 6, 6):
    if word[i:i + 6] in change.keys():
        result += change[word[i:i + 6]]
    else:
        new_word = word[i:i + 6]
        tmp = ''
        for key in change.keys():
            check = bin(int(key, 2) ^ int(word[i:i + 6], 2))
            if check.count('1') == 1:
                tmp += change[key]

        if tmp:
            result += tmp
        else:
            print(i // 6 + 1)
            break
else:
    print(result)