#Write a program to calculate the sum of the first n natural numbers
n=int(input("Enter n:"))
total=0
for i in range(1,n+1):
    total +=i
    print("sum=",total)