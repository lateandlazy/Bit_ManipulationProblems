def countSetBits(n):
    i=0
    a=0
    while ((1 << i) <= n):
        k=0
        m = 1 << i
        for j in range(0,n+1):
            a += k
            if m == 1:
                k = not k
                m = 1 << i
            else:
                m -= 1
        i += 1
    return a
x = int(input("Enter the Number:"))
print(countSetBits(x))
