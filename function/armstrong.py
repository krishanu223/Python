num=int(input())
def armstrong(num):
    sum=num%10
    sum1=num%10
    num1=num
    num2=num
    h=0
    i=0
    addition=0
    while i==0 :
        num2=num2//10
        h=sum  
        sum=num2%10
        i=i+1
    while num1 !=0:
        num1=num1//10 
        addition=addition+sum1**h
        sum1=num1%10  
    return addition   

    
arm=armstrong(num)
if arm==num:
    print("This is armstrong number")
else:
    print("not a armstrong number")
