def solution(n):
    arr = list(map(int, n))
    arr.sort()
    arr.reverse()
    for i in arr:
        print(i, end='')
if __name__ == '__main__':
    n = str(input())
    solution(n)
