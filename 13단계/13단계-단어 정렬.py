import sys
def solution(n):
    arr = list()
    for i in range(n):
        arr.append(str(input()))
    arr2 = list(set(arr))
    arr2 = sorted(arr2, key = lambda x: (len(x), x))

    for i in arr2:
        print(i)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    solution(n)
