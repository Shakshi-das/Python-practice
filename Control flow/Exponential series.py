#program to calculate the value of x in e^x series

x=float(input("enter the value of x:"))
n=int(input("enter the value of n:"))
s=1
for i in range(1,n+1):
    p=x**i
    f=1
    for j in range(1,i+1):
        f=f*j
    term=(p/f)
    s=s+term
print("e^",x,"is",round(s,3))
