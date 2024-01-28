num=int(input())
i=0
while i<= num:
    j=0
    while j<i:
        char=chr(ord("A")+((num-i)+j))
        print(char,end="")
        j=j+1
    print()
    i= i+1