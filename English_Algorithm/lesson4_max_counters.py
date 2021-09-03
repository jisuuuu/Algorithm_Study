#MaxCounters
def solution(N, A):
    # write your code in Python 3.6
    result = [0 for _ in range(N)]
    max_num = 0

    for a in A:
        if 1 <= a <= N:
            result[a - 1] += 1

            if max_num < result[a - 1]:
                max_num = result[a - 1]
        elif a == N + 1:
            result = [max_num for _ in range(N)]

    return result


# O(N*M) 오답 3개

def solution(N, A):
    # write your code in Python 3.6
    li = {i: 0 for i in range(1, N + 1)}
    max_sum = 0
    max_num = 0
    for key in A:
        if key == N + 1:
            max_sum += max_num
            li.clear()
            max_num = 0
        else:
            if li.get(key) is None:
                li[key] = 1
            else:
                li[key] += 1

            max_num = max(max_num, li[key])

    answer = [max_sum] * N
    # li = sorted(li)
    for key, val in li.items():
        answer[key - 1] += val

    return answer