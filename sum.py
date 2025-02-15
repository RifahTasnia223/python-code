num = int(input("input any number: "))
sum = 0
for i in range(1, num+1): 
    sum += i
print(sum) 

n=input("enter a number:")
d=input("enter any number:")
while(n>0):
    if(n%10==d):
        count=count+1
        n=n//10
print()
