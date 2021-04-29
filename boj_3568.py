#iSharp
import sys

string_list = sys.stdin.readline().rstrip().split(' ')

basic_type = string_list[0]
del string_list[0]


for s in string_list:
    res = ''
    s = s.replace(',', '').replace(';', '')

    res += basic_type

    for i in range(len(s) - 1, 0, -1):
        if not s[i].isalpha():
            if s[i] == ']':
                res += '['
            elif s[i] == '[':
                res += ']'
            else:
                res += s[i]

    res += ' '

    for i in range(len(s)):
        if s[i].isalpha():
            res += s[i]

    res += ';'
    print(res)