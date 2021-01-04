
'''Exercise 10.9. Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original.'''






def remove_duplicates(s):
    k = []
    for a in s:
        if a not in k:
            k.append(a)
    return k

    
print(remove_duplicates([1, 2,2, 3, 4, 4, 6, 6, 7, 5, 10]))
