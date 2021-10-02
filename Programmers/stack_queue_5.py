#스택/큐 - 주식가격
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []

    for i, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            s = stack.pop()
            answer[s] = i - s
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer