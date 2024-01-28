liinput=input().split()
ele=int(input())
print(len(liinput))

for i in range (0,len(liinput)):
    if int(liinput[i])==ele:
        print("the number of position:",i)