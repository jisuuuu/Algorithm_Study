#크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack = []

    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                if stack:
                    if stack[-1] == board[i][m - 1]:
                        answer += 2
                        stack.pop()

                        board[i][m - 1] = 0
                        break

                stack.append(board[i][m - 1])
                board[i][m - 1] = 0
                break

    return answer