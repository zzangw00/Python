a, b, c = map(int, input().split())
mid = 0

if a >= b and a <= c:
    mid = a
elif a <= b and a >= c:
    mid = a

if b >= a and b <= c:
    mid = b
elif b <= a and b >= c:
    mid = b

if c >= a and c <= b:
    mid = c
elif c <= a and c >= b:
    mid = c

print(mid)
