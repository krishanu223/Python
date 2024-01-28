num=int(input())
for i in range (num,0,-1):
    if i%2==0:

        for j in range (0,i):
            print("1",end="")
    else:
        for j in range (0,i):
            print("0",end="")
    print()
