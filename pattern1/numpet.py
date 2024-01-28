N = int(input())
i=1
while i<=N:
    j=N
    while j>=i:
        print(N-j+1,end="")
        j=j-1
    i=i+1
    print()