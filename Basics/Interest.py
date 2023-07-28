#program to calculate simple and compound interest

p=int(input("enter principle amount:"))

r=float(input("enter rate:"))

t=int(input("enter time period in years:"))

s=(p*r*t)/100

a=p*((1+r/100)**t)

c=(a-p)

s=print("the simple interest is:",s)

c=print("the compound interest is:",c)
