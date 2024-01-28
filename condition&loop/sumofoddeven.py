# input1=int(input())
# even=0
# odd=0
# base=0;
# while base<input1:
#     print(base)
#     if base%2:
#         even=even+base
#     else:
#         odd=odd+base
#     base=base+1
# print("odd",even)
# print("even",odd)

l=list(input())
e,o=0,0
for i in l:
    if int(i)%2==0:
        o=o+int(i)
    else:
        e=e+int(i)
print(o,e,sep='   ')