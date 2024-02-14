#program to count the number of vowels and consonants

str=input("please enter a string : ")
vowels=0
consonants=0

for i in range(0,len(str)):

    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' or str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U'):

        vowels=vowels+1

    else:

        consonants=consonants+1

print("the number of vowels is",vowels)
print("the numer of consonants is",consonants)
