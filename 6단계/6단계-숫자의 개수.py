arr = []
for i in range(3):
    arr.append(int(input()))

result = arr[0] * arr[1] * arr[2]
arr1 = str(result)

for i in range(10):
    print(arr1.count(str(i)))