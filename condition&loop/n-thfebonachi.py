n = int(input())
a=0
b=1
c=0
i=0
while i < n:
     a=b
     b=c
     c=a+b
     i=i+1
print(c)
