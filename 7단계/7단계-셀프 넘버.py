def solve(n):
    return n+sum([int(i) for i in str(n)])
arr=[0]*10000

for i in range(10000):
    if(solve(i)<10000):
        arr[solve(i)]=1

for i in range(10000):
    if arr[i]==0:
        print(i)
