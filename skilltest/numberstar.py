n = int(input())
for i in range(0, n):
    for j in range(n, i+1, -1):
        print(j, end="")
    for k in range(0, 1):
        print("*", end="")
    for l in range(i, 0, -1):
        print(l, end="")
    print()
