def countSetBits(n):
    count= 0
    while n:
        count += 1
        n &= (n-1)
    return count

def flipCount(x,y):
    m = countSetBits(x ^ y)
    return m
a = int(input("Enter A:"))
b = int(input("Enter B:"))
print(flipCount(a,b))