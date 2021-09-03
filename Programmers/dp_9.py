#가장 큰 정사각형
def solution(board):
    answer = board[0][0]
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j], min(board[i - 1][j - 1], board[i][j - 1])) + 1

                answer = max(answer, board[i][j])
    return answer * answer