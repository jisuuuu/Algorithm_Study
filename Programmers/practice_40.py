#배열의 유사도
def solution(s1, s2):
    return len(set(s1).intersection(s2))


if __name__ == '__main__':
    print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
    print(solution(["n", "omg"], ["m", "dot"]))