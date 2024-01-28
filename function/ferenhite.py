def printTable(start,end,step):
	while start<=end:
		start=start+step
		print(start-step,end=" ")
		print(int(5/9*(start-20-32)))
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





