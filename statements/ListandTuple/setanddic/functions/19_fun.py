#write a program for recursive function to calculate factorial of a number
def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
count(5)