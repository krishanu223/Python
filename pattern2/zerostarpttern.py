num=int(input())
i=1
while i<=num:
    j=0
    k=num
    l=num
    o=0
    while j<i:
        if j==i-1:
            print("*",end="")
        else:
            print("0",end="")
        j=j+1
    while k>=i:
        if k==i:
            print("*",end="")
        else:
            print("0",end="")
        k=k-1
    while l>=i:
        if l==i:
            print("*",end="")
        else:
            print("0",end="")
        l=l-1
    while o<i-1:
        print("0",end="")
        o=o+1
    print()    
    i=i+1