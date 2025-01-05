def setBits(a):
    count=0
    while (a):
        count += a & 1
        a >>= 1
    return count
x = int(input("Enter the Number:"))
print(setBits(x))