num=int(input())
def palidrome(num):
    temp=num
    rev=0
    while temp!=0:
        rev=(rev*10)+(temp%10)#reverse input number
        temp=temp//10
    if rev==num:
        return True
    else:
        return False
print(palidrome(num))