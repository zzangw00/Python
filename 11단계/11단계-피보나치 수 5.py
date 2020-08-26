def solution(a):
    if a <= 1:
        return a
    return solution(a - 1) + solution(a - 2)

if __name__ == '__main__':
    a = int(input())
    print(solution(a))