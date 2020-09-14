def solution(n):
    arr = []
    for i in range(n):
        arr.append(list(map(str, input().split())))
    arr = sorted(arr, key = lambda x: (int(x[0])))
    for x, y in arr:
        print(x, y)

if __name__ == '__main__':
    n = int(input())
    solution(n)