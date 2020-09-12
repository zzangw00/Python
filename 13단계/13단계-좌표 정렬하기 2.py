import sys
def solution(n):
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr = sorted(arr, key = lambda x: (x[1], x[0]))

    for i, j in arr:
        print(i, j)
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    solution(n)
