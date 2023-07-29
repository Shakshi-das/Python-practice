#program to display first n even numbers

n even numbers
n=int(input("enter the range:"))
for i in range(1,n+1,1):
    if i%2==0:
        print(i)
