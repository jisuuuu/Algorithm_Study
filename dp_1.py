#N으로 표현
answer = -1
def solution(n, number):
    dfs(0, 0, n, number)
    return answer

def dfs(cnt, prev, n, number):
    temp = n
    global answer

    if cnt > 8:
       answer = -1
       return

    if number == prev:
        if answer == -1 or answer > cnt:
            answer = cnt
        return

    for i in range(1, 8 - cnt + 1):
        dfs(cnt + i, prev + temp, n, number)
        dfs(cnt + i, prev - temp, n, number)

        if prev != 0:
            dfs(cnt + i, prev * temp, n, number)
            dfs(cnt + i, prev / temp, n, number)

        temp = temp * 10 + n