num=int(input())
for i in range(num):
    for j in range(1,i+2):
        # print("value:",i+1,"value:j",j)
        print(num-j+1,end="")
    for k in range (num-i-1,0,-1):
        print(num-i,end="")
    for l in range(num-1,i,-1):
        print(num-i,end="")
    for m in range (0,i):
        print((num-i)+m+1,end="")
    print()
for i in range(num-1):
    for j in range (num-i,1,-1):
        print(i+j,end="")
    for k in range (0,i+1):
        print(i+2,end="")
    for l in range (0,i):
        print(i+2,end="")
    for m in range((num-i)-1,0,-1):
        print((num-m)+1,end="")
    print()
