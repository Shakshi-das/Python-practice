#program to check if a number is strong or not

Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("Factorial of ", Factorial)
    Sum = Sum + Factorial
    Temp = Temp // 10

print("Sum of Factorials of a Given Number =", Sum)
    
if (Sum == Number):
    print(" is a Strong Number" ,Number)
else:
    print(" is not a Strong Number",Number)
