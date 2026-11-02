#Write a program to keep asking for a number until the user enters zero
while True:
    n = int(input("Enter a number:"))
    if n == 0:
        break
    print("Program stopped")
    