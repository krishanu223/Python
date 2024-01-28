arr=[5,7,9,2,4,10]
n=len(arr)+1
for i in range(n):
    minindex=i
    for j in range (i+1,n-1):
        if arr[j]<arr[minindex]:
            minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
        print(arr)

# logic of binarry search 