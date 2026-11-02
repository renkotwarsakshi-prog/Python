#Write a program to search for anumber in a list and stop when it is found
numbers = [10,20,30,40,50]
n = int(input("Enter number to search:"))
for i in numbers:
    if i == n:
        print("Number found")
        break
    
else:
  print("Number not found")