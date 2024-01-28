
def findGcd(x, y):
    # Write your code here
    # Return an integer
    while y:
        print(y)
        x, y = y, x % y
        print(x)
    return x

a=findGcd(15, 20)
print(a)
