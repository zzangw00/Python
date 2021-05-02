def solution(n):
    arr = []
    for i in range(n):
        arr.append(int(input()))

    arr.sort()
    for i in arr:
        print(i)
if __name__ == '__main__':
    n = int(input())
    solution(n)