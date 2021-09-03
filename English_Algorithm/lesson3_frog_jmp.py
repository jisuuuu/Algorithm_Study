def solution(X, Y, D):
    # write your code in Python 3.6
    return (Y - X) // D if (Y - X) % D == 0 else (Y - X) // D + 1
# 거리 Y - X