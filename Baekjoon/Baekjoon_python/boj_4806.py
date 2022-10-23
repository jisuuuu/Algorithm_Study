#줄 세기
total = 0

while True:
    try:
        s = input()
        total += 1
    except EOFError:
        break
print(total)