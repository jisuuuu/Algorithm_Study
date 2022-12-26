#이진수 더하기
def solution(bin1, bin2):
    return format(int(bin1, 2) + int(bin2, 2), 'b')


if __name__ == '__main__':
    print(solution('10', '11'))
    print(solution('1001', '1111'))