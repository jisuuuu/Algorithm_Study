#단어 변환
answer = 0


def solution(begin, target, words):
    visited = [0 for _ in range(0, len(words))]

    for i in range(0, len(words)):
        if compare(target, words[i]) == 0:
            dfs(begin, words, visited, i, 1)

    global answer
    return answer


def compare(s1, s2):
    cnt = 0

    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            cnt += 1

    return cnt


def dfs(now, words, visited, idx, depth):
    global answer
    if compare(now, words[idx]) == 1:
        if answer == 0:
            answer = depth
        else:
            answer = min(answer, depth + 1)

        return

    visited[idx] = 1

    for i in range(0, len(words)):
        if compare(words[idx], words[i]) == 1 and visited[i] == 0:
            dfs(now, words, visited, i, depth + 1)