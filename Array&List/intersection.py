arr=[1,2,3,4,5]
arr1=[1,2,8,9,5]
inter=[]
for i in range (len(arr)):
    for j in range(len(arr1)):
        if arr[i] == arr1[j]:
            inter.append(arr1[j])
print("common number of two arr:",inter)