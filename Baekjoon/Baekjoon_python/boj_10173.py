#니모를 찾아서
import sys
while True:
    word = sys.stdin.readline().rstrip()

    if word == 'EOI':
        break

    if word.upper().find('NEMO') != -1:
        print('Found')
        continue
    print('Missing')