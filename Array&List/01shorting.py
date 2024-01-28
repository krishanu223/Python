li=[0,1,1,0,0,1,0]
zero=0
for i in range(len(li)):
    if li[i]==0:
         temp=li[zero]
         li[zero]=li[i]
         li[i]=temp
         zero = zero+ 1 
print(li)        
        
