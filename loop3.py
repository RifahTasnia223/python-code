
n = int(input("Enter the upper range: "))
print(f"Even numbers between 1 to {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:
        if i < n and i != n - 1:
            print(i, end=", ")

    else:
        print(i)  
