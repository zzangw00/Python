def solution(a):
    for i in range((a // 3) + 1):
        for j in range((a // 5) + 1):
            if 5 * j + 3 * i == a:
                return i + j
    return -1

if __name__ == '__main__':
    a = int(input())
    print(solution(a))