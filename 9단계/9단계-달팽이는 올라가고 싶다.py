a, b, v = map(int, input().split())
c = (v - b) / (a - b)
if c == int(c):
    print(int(c))
elif c != int(c):
    print(int(c + 1))
