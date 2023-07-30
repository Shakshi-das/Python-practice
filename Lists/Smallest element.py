#program to find the smallest element in a list

#using standard function

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))

for i in range(1, Number + 1):

    value = int(input("Please enter the Value of Element : ",i))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))

#not using standard function

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))

for i in range(1, Number + 1):

    value = int(input("Please enter the Value of Element : " ,i))
    NumList.append(value)

NumList.sort()
print("The Smallest Element in this List is : ", NumList[0])
