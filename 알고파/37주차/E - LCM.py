import sys
n = int(sys.stdin.readline())

def gcd(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a

for i in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))