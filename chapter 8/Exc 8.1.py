'''Exercise 8.10. A string slice can take a third index that specifies the “step size;” that is, the number
of spaces between successive characters. A step size of 2 means every other character; 3 means every
third, etc.
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.'''



def palindrome(string):
    string = str(string)    
    return string == string[::-1]

print(is_palindrome('banana'))
print(is_palindrome('MoM'))
print(is_palindrome('Friends'))
print(is_palindrome('Middle'))
print(is_palindrome('Laptop'))
