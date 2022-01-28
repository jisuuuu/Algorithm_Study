#문서 검색
import sys
document = list(sys.stdin.readline().rstrip())
check = list(sys.stdin.readline().rstrip())
i = 0
cnt = 0

while i <= len(document) - len(check):
    if document[i:i + len(check)] == check:
        cnt += 1
        i += len(check)
    else:
        i += 1
print(cnt)