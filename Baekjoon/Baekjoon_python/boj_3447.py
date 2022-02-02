#버그왕
import sys
import re
code = sys.stdin.readlines()

for c in code:
    while True:
        result = re.sub('BUG', '', c)

        if 'BUG' in result:
            c = result
        else:
            print(result, end='')
            break