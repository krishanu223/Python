num=int(input())
def febo(num):
    a=0
    b=1
    c=0
    for i in range (1,num):
        a=i
        b=c
        c=a+b
        if num==c:
            return True
        break   
febo(num)
if febo(num==True):
    print("true")
else :
    print("false")
