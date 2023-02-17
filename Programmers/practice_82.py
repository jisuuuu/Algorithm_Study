#가위 바위 보
def solution(rsp):
    game = {'2': '0', '0': '5', '5': '2'}
    return ''.join([game[s] for s in rsp])


if __name__ == '__main__':
    print(solution('2'))
    print(solution('205'))