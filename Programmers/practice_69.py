#특이한 정렬
def solution(numlist, n):
    numlist.sort(reverse=True)
    return sorted(numlist, key=lambda x:abs(x - n))


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6], 4))
    print(solution([10000,20,36,47,40,6,10,7000], 30))