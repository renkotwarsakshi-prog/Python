#Write a program to count the frequency of each word in a  string using dictionary
string ="hello"
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] +=1
    else:
        frequency[char]=1
        
print(frequency)