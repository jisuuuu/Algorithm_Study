#네트워크

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(0, n)]

    for idx, v in enumerate(visited):
        if v == False:
            answer += 1
            dfs(idx, visited, computers)

    return answer

def dfs(idx, visited, computers):
    visited[idx] = True

    for i in range(0, len(computers)):
        if visited[i] == False and computers[idx][i] == 1:
            dfs(i, visited, computers)

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))