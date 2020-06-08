#오픈채팅방
def solution(record):
    answer = []
    user = dict()
    chatlog = []

    enterMsg = "%s님이 들어왔습니다."
    exitMsg = "%s님이 나갔습니다."

    for r in record:
        info = r.split(' ')

        if info[0] == 'Enter':
            user[info[1]] = info[2]
            chatlog.append([enterMsg, info[1]])

        elif info[0] == 'Leave':
            chatlog.append([exitMsg, info[1]])

        elif info[0] == 'Change':
            user[info[1]] = info[2]

    for c in chatlog:
        answer.append(c[0] % user[c[1]])

    return answer