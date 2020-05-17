#타켓 넘버
answer = 0


def solution(numbers, target):
    dfs(numbers, target, 0)
    return answer


def dfs(numbers, target, idx):
    global answer
    if idx == len(numbers):
        sum = 0

        for n in numbers:
            sum += n

        if sum == target:
            answer += 1
        return

    else:
        numbers[idx] *= 1
        dfs(numbers, target, idx + 1)

        numbers[idx] *= -1
        dfs(numbers, target, idx + 1)