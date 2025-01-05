def square(n):
    if (n == 0):
        return 0
    if (n < 0):
        n = -n

    m = n >> 1
    if (n & 1):
        return ((square(m) << 2) + (m << 2) + 1)
    else:
        return (square(m) << 2)

a = int(input("Enter the Number:"))
print("The square of the Number is:",square(a))