#전화번호 목록
def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if i == j:
                continue

            if phone_book[i] in phone_book[j]:
                return False
    return True