li=[1,2,34,5]
# li1=[]
# for i in range(len(li)-1,-1,-1):
#     li1.insert(len(li)-i,li[i])
# print(li1)
for i in range(0,len(li)//2):
    # li[i-1]=li[len(li)-i-1]
    li[i], li[len(li)-i-1] = li[len(li)-i-1] ,li[i]
print(li)