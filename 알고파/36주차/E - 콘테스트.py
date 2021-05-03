arr1 = []
arr2 = []
for i in range(0, 10):
    a = int(input())
    arr1.append(a)
for i in range(0, 10):
    b = int(input())
    arr2.append(b)
arr1.sort(reverse=True)
arr2.sort(reverse=True)
arr1sum = 0
arr2sum = 0
for i in range(0, 3):
    arr1sum += arr1[i]
    arr2sum += arr2[i]
print(arr1sum, arr2sum)