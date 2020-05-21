#타켓 넘버
answer = 0


def solution(numbers, target):
    dfs(numbers, target, 0)
    return answer


def dfs(numbers, target, idx):
    global answer
    if idx == len(numbers):
        if sum(numbers) == target:
            answer += 1
        return

    else:
        numbers[idx] *= 1
        dfs(numbers, target, idx + 1)

        numbers[idx] *= -1
        dfs(numbers, target, idx + 1)