#Write a program to reverse a number
n=int(input("Enter a number:"))
num=abs(n)
rev=0
while num>0:
    digit = num%10
    rev = rev*10 + digit
    num //=10
if n<0:
    rev = -rev
print("Reversed number =",rev)