#Write a function to count vowels in a given string
def count_vowels(s):
    count=0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    print("Number of vowels:",count)
count_vowels("hello world")