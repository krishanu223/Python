num=int(input())
i=1
while i<num+1:
    j=0
    while j<i:
        x=i-1
        if x==0:
            print(1,end="")
        else:
            if x==j or j==0 :
                print(x,end="")
            else:
                print(0,end="")
        j=j+1    
    print()
    i=i+1
    #logic-run on which nested loop print number of this loop