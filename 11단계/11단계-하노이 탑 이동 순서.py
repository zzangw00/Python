def solution(a, start, mid, end):
    if a == 1:
        print(start, end)
        return
    solution(a - 1, start, end, mid)
    print(start, end)
    solution(a - 1, mid, start, end)


if __name__ == '__main__':
    a = int(input())
    print((2 ** a) - 1)
    solution(a, 1, 2, 3)