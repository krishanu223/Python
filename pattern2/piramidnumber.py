# n = int(input())
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(i, 0, -1):
#         print(j, end="")
#     for k in range(2, i+1):
#         print(k, end="")
#     print()
num=int(input())
i=0
while i<num:
    j=0
    s=0
    p=i
    k=0
    d=2
    while j<num-i-1:
        print(" ",end="")
        j=j+1
    while p>=k:
        print(p+1,end="")
        p=p-1
    while d<i+2:
        print(d,end="")
        d=d+1
    print()
    i=i+1