'''
Exercise 4.1

1. Write appropriate docstrings for polygon, arc and circle.
2. Draw a stack diagram that shows the state of the program while executing circle(bob,
radius). You can do the arithmetic by hand or add print statements to the code.
3. The version of arc in Section 4.7 is not very accurate because the linear approximation of the
circle is always outside the true circle. As a result, the turtle ends up a few units away from
the correct destination. My solution shows a way to reduce the effect of this error. Read the
code and see if it makes sense to you. If you draw a diagram, you might see how it works.
'''


def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    return check_fermat(a, b, c, n)

check_numbers()