#program to input marks and assign grades to students

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))

total=(sub1+sub2+sub3+sub4+sub5)

if(total>=90):
    print("Grade is outstanding")

elif(total>=80):

    print("Grade is excellent")

elif(total>=70):

    print("Grade is fine")

elif(total>=60):

    print("Grade is good")

elif(total>=50):

    print("Grade is average")

elif(total>=40):

    print("Grade is just pass")

elif:

    print("Fail")

else:
    print("invalid input")
