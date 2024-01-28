num=int(input())
i=0
while i<=num:
    j=0
    while j<=i:
        charp=chr(ord('A')+i+j)
        print(charp,end="")
        j=j+1
    print()
    i=i+1