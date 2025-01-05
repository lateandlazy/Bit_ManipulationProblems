def powerOfTwo(x):
    if (x == 0):
        return 0
    if ((x & (~(x-1))) == x):
        return 1
    return 0
if __name__ == "__main__":
    a = int(input("Enter the Number:"))
    if (powerOfTwo(a)):
        print("Yes")
    else:
        print("No")