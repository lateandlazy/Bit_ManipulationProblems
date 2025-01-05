def nonRepeatingNo(n):
    diff= 0
    for i in n:
        diff ^= i
    diff &= -diff
    m = [0, 0]
    for i in n:
        if (i & diff) == 0:
            m[0] ^= i
        else:
            m[1] ^= i

    if m[0] > m[1]:
        m[0], m[1] = m[1], m[0]
    return m
arr = [2,4,3,2,4,5]
res = nonRepeatingNo(arr)
print("The numbers are :",res[0],"and",res[1])