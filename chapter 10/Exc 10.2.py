'''Exercise 10.3. Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6]'''


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def List_fun(num):
    sums = []
    total = 0
    for i in num:
        total += i
        sums.append(total)
    print (sums)

List_fun(num)
