#2018 KAKAO BLIND RECRUITMENT [3차] n진수 게임

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    answer = ''
    num = 0
    result = ''
    result_len = 0
    while True:
        cvt_num = convert(num, n)
        result += cvt_num
        result_len += len(cvt_num)

        # t 1000이하 m 100이하 가장 큰 수는 t * m인 100000번째 수 그걸 넘어가면 break
        if result_len > 100001:
            break
        num += 1

    answer += result[p - 1 : t * m : m]

    return answer


if __name__ == '__main__':
    print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))
    print(solution(16, 16, 2, 2))