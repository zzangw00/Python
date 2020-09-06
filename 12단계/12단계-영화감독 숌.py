def solution(n):
    a = 666
    count = 0
    while True:
        if '666' in str(a):
            count += 1
            if n == count:
                print(a)
                break
        a += 1
if __name__ == '__main__':
    n = int(input())
    solution(n)