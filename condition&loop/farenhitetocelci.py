#custom test

# startindex=int(input())
# endindex=int(input())
# stepsize=int(input())
# while startindex<=endindex:
#     print(startindex,int((startindex-32)*5/9))
#     startindex=startindex+stepsize
startindex=int(input())
endindex=int(input())
stepsize=int(input())
while startindex<=endindex:
    c=(startindex-32)*5/9
    c=int(c)
    print(startindex,c)
    startindex=startindex+stepsize
   
