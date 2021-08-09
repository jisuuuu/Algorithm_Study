#베스트 셀러
import sys
n = int(sys.stdin.readline().rstrip())
books = dict()

for _ in range(n):
    title = sys.stdin.readline().rstrip()

    if title in books.keys():
        books[title] += 1
    else:
        books[title] = 1

result = sorted(books.items(), key=(lambda x:(-x[1], x[0])))
print(result[0][0])