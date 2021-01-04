
'''Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes
a nested list of strings and returns a new nested list with all strings capitalized.'''


def capitalize(listt):
    capitalized = []
    for i in listt:
        if type(i) is list:
            i = capitalize(i)
        else:
            i = i.capitalize()  
        capitalized.append(i)
    return capitalized

print(capitalize(['a','b','c']))
print(capitalize(['a','b','c',['a','a'],['a']]))
print(capitalize([]))
print(capitalize([['Apple'],['melon'],['water'],['potato'],['lime'],['tomato']]))
