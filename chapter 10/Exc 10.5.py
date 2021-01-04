'''Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.'''

str1 = "Yoga"
str2 = "Lakshmi"


def is_anagram(str1, str2):
    
    if(sorted(str1) == sorted(str2)):
       print("Anagrams")
    else:
       print("Not Anagrams") 

is_anagram(str1, str2)
