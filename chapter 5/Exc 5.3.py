''' Exercise 5.3. Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
a
n + b
n = c
n
for any values of n greater than 2.
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and that
checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
a
n + b
n = c
n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
'''




def check_fermat(a, b, c, k):
    if k > 2 and (a**k + b**k == c**k):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    k = int(input("Choose a number for k: "))
    return check_fermat(a, b, c, k)

check_numbers()
