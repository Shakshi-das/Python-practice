#program to print Floyd's triangle pattern of numbers

n=int(input("enter the num of rows:"))

k=1

for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=" ")

        k=k+1

    print("\n")
