H, M = map(int, input().split())

if H > 0 and H < 24:
    if M >=45 and M < 60:
        print(H, (M - 45))
    else:
        print((H - 1), ((60 + M) - 45))

elif H == 0:
    if M >=45 and M < 60:
        print(H, M - 45) 
    else:
        print(23, ((60 + M) - 45))
