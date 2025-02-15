n = int(input("Enter the upper limit: "))
sum_odd = 0

for i in range(1, n + 1):
    if i % 2 != 0: 
        sum_odd += i  
print(f"Sum of odd numbers from 1 to {n}: {sum_odd}")
