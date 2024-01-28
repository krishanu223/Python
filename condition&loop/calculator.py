o=int(input())
while o!=6:
    if o<=5 and o>=1:
       a=int(input())
       b=int(input())
    if o==1:
        print(a+b)
    if o==2:
        print(a-b)
    if o==3:
        print(a*b)
    if o==4:
        print(a//b)
    if o==5:
        print(a%b)
    elif o>6 or o<1: #work only when enter invalid number
       print("Invalid Operation") 
    o=int(input())# input again

