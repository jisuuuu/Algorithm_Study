def solution(N):
    # write your code in Python 3.6
    binary = format(N, 'b') # bin() 이걸로 하면 안 먹는 것 있음 이걸로
    max_num = 0
    cnt = 0

    for b in binary:
        if b == '1':
            if max_num < cnt:
                max_num = cnt
            cnt = 0
        else:
            cnt += 1

    return max_num