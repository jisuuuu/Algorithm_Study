#예산
def solution(budgets, M):
    answer = 0
    maxs = max(budgets)
    mins = 0

    while mins <= maxs:
        mid = int((mins + maxs) / 2)

        temp = [b if b < mid else mid for b in budgets]

        if sum(temp) > M:
            maxs = mid - 1
        elif sum(temp) <= M:
            mins = mid + 1
            answer = mid

    return answer