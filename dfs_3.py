min = 0
def solution(begin, target, words):
    answer = 0
    visited = [0 for i in range(0, len(words))]

    for i in range(len(words) - 1, 0, -1):
        if compare(target, words[i]) == 0:
            dfs(begin, words, visited, i, 1)

    global min
    answer = min
    return answer
def compare(s1, s2):
    cnt = 0

    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            cnt += 1

    return cnt

def dfs(now, words, visited, idx, depth):
    global min
    if compare(now, words[idx]) == 1:
        if min == 0:
            min = depth
        else:
            min = min(min, depth + 1)

    visited[idx] = 1

    for i in range(0, len(words)):
        if compare(words[idx], words[i]) == 1 and visited[i] == 0:
            dfs(now, words, visited, i, depth + 1)