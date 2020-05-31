#[1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []

    for a in arr1:
        new = format(a, 'b')

        s = ""
        if len(new) != n:
            for _ in range(n - len(new)):
                s += "0"
        new = s + new

        real = ""
        for w in new:
            if w == '0':
                real += " "
            elif w == '1':
                real += "#"

        answer.append(real)

    for i in range(len(arr2)):
        new = format(arr2[i], 'b')

        s = ""
        if len(new) != n:
            for _ in range(n - len(new)):
                s += "0"
        new = s + new

        for j in range(len(answer[i])):
            if answer[i][j] == " " and new[j] == '1':
                answer[i] = answer[i][0: j] + "#" + answer[i][j + 1:]

    return answer