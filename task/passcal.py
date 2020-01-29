def f(n):
    res = 1
    for c in range(1, n + 1):
        res = res * c
    return res
r = int(input("Enter the number of rows : "))
for i in range(0, r):
    for j in range(1, r - i):
        print("  ", end="")
    for k in range(0, i + 1):
        coff = int(f(i) / (f(k) * f(i - k)))
        print("  ", coff, end="")
    print()