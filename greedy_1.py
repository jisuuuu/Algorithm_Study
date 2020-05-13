#체육복
def solution(n, lost, reserve):
    #도난 당한 사람과 여분을 갖고 온 사람이 겹칠 수 있으므로 제거
    new_reserve = [r for r in reserve if r not in lost]
    new_lost = [l for l in lost if l not in reserve]

    for r in new_reserve:
        f = r - 1
        b = r + 1

        if f in new_lost:
            new_lost.remove(f)
        elif b in new_lost:
            new_lost.remove(b)

    return n - len(new_lost)