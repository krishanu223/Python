num=int(input())
i=0
while i<num:
    s=0
    j=1
    r=0
    while s<num-i-1:
        print(" ",end="")
        s=s+1
    while j<=i+1:
        print("*",end="")
        j=j+1
    while r<=i-1:
        print("*",end="")
        r=r+1
    print()
    i=i+1