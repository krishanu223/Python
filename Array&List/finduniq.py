arr=[1,2,1,7,2,3,3]
for i in range (len(arr)):
    j=0
    while j<len(arr):
        if i == j and arr[i] == arr[j]:
            break
        j=j+1
        if j==len(arr):
            print(arr[i])
   

 