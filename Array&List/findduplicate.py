arr=[1,2,1,2,4,5]
count = 1
for i in range(0, len(arr)):
    if arr.count(arr[i]) > count:
        res = arr[i]
print(res)
        