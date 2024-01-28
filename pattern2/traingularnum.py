n = int(input())
i = 0
while i < n:
    sp = 1
    nu = 0
    #speacing
    while sp < n-i:
        print(" ", end='')
        sp = sp+1
    #staring
    while nu <= i:
        print(nu+1+i, end='')
        nu = nu+1
    #repeat star
    b =nu-1
    while b >=1:
        print(b+nu-1, end='')
        b = b-1
    print()
    i = i+1