#더하기 2
total = ''

while True:
    try:
        total += input()
    except EOFError:
        break
print(sum(map(int, total.split(','))))