# Implement a  program to check the count of vowels in a given string.(with repeated occurance
string=input("enter the string")
vowels =0;
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:",vowels)
