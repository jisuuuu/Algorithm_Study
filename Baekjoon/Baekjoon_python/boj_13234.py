#George Boole
import sys
words = sys.stdin.readline().rstrip().split(' ')

if words[1] == 'AND':
    if words[0] == 'false' or words[2] == 'false':
        print('false')
    else:
        print('true')
else:
    if words[0] == 'true' or words[2] == 'true':
        print('true')
    else:
        print('false')