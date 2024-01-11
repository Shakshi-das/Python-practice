#program to calculate value of x in cosx series

y=float(input("enter the value of x:"))
n=int(input("enter the value of n:"))
x1=(3.14285*x)/180
s=0
k=0
for i in range(1,n+1):
    p=x**i
    f=1
    for j in range(1,i+1):
        f=f*j
    term=((-1)**k)*(p/f)
    k=k+1
    s=s+term
print("cos",x,"is",round(s,2))
