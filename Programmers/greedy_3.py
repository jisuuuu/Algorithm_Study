#큰수 만들기
def solution(number, k):
    # 1. 스택 생성
    stack = []

    # 2. 큰 수가 앞자리가 되게끔 스택에 저장합니다.
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1

        stack.append(n)

    # 3. k가 남았다면 뒤에서부터 뺍니다.
    while k > 0:
        stack.pop()
        k-=1

    answer = "".join(stack)
    return answer