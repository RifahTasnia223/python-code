n=int(input("input any number:"))
if n>1:
  is_prime=True
  for i in range(2,n):
     if n%i==0:
        is_prime=False
        break
if is_prime:
        print(f"{n}this is prime number.")
else:
        print(f"{n}this is not prime.")

