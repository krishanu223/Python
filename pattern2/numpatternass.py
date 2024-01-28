n = int(input())
i=1
while i<=n:
    j=1
    h=n+2
    p=1
    while j<=i:
        print(j,end="")
        j=j+1
    while h > i-1:
        print(" ", end="")
        h = h-1
    while p <= i:
        print(p+i-1, end="")
        p = p+1
    print()
    i=i+1
