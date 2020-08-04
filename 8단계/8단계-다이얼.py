arr = input()
sum = 0
al = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'
arr_s = list(al.split())
for i in arr:
    for j in arr_s:
        if i in j:
            sum += (arr_s.index(j) + 3)
print(sum)