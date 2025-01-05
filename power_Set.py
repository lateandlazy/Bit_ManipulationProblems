def setElements(s):
    x = len(s)
    r = []
    for i in range(1 << x):
        subset = ""
        for j in range(x):
            if i & (1 << j):
                subset += s[j]
        r.append(subset)
    return r
if __name__ == "__main__":
    str = input("Enter the string:")
    subsets = setElements(str)

    for m in subsets:
        print(m)