num=int(input())
temp = num
rev=0
while temp!=0:
    rev=(rev*10)+(temp%10)#reverse input number
    temp=temp//10

if(num==rev):#compearing input to rev
    print('true')
else:
    print('false')
