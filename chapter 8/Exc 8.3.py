'''Exercise 8.12. ROT13 is a weak form of encryption that involves “rotating” each letter in a word
by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the
beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.
Write a function called rotate_word that takes a string and an integer as parameters, and that
returns a new string that contains the letters from the original string “rotated” by the given amount.
For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
You might want to use the built-in functions ord, which converts a character to a numeric code,
and chr, which converts numeric codes to characters.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily
offended, find and decode some of them.'''


import string


def rotate_letter(let, n):
    
    if let.upper():
        start_word = ord('A')
    elif let.lower():
        start_word = ord('a')
    else:
        return let

    k = ord(let) - start_word
    i = (k + n) % 26 + start_word
    return chr(i)


def rotate_word(word, n):
    
    result = ''
    for let in word:
        result = result + rotate_letter(let, n)
    return result


print(rotate_word('yoga', 7))
print(rotate_word('laptop', -10))
print(rotate_word('work', 9))
