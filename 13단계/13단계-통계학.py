import sys
def r1(arr, n):
    sum1 = 0
    for i in arr:
        sum1 += i
    result = sum1 / n
    print(int(round(result, 0)))

def r2(arr, n):
    arr.sort()
    print(arr[n // 2])

from collections import Counter
def r3(arr, n) :
    if n == 1 : return arr[0]
    c = Counter(arr).most_common(2)
    return ((c[1][0] if c[0][1] == c[1][1] else c[0][0]))


def r4(arr, n):
    print(max(arr) - min(arr))
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    r1(arr, n)
    r2(arr, n)
    print(r3(arr, n))
    r4(arr, n)