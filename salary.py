def fun(a, b,c):
    return (a,b+(c*0.15))
a=str(input())
b = float(input())
c= float(input())
e = fun(a,b,c)
print(f"TOTAL = R$ {e:.2f}")