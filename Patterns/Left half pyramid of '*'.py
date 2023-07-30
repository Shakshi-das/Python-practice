#program to print a left half pyramid

n=int(input("enter the number of rows:"))

for i in range (1,n+1):

    for k in range (n,i,-1):
        print(" ",end=" ")

    for j in range (1,i+1):
        print("*",end=" ")

    print("\n")
