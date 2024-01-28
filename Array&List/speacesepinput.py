# str_input=input()
# str_inputslite=str_input.split()
# print(str_inputslite)
# li=[]
# for i in str_inputslite:
#     li.extend([int(i)])
# print(li)
li=[ int(x) for x in input().split()] # single line input and convert to array
print(li)