inputnumber=int(input())
z=inputnumber%10
inputnumber=inputnumber//10 
sum=z*10
while inputnumber>=10:
    z=inputnumber%10
    sum=(sum+z)*10
    inputnumber=inputnumber//10 
print(sum+inputnumber)