#K번째수
def solution(array, commands):
    answer = []
    for command in commands:
        new = [array[i] for i in range(command[0] - 1, command[1])]
        new.sort()
        answer.append(new[command[2] - 1])

    return answer