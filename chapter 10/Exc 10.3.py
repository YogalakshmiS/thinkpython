'''Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc.
'''


def sort(list):
    if sorted(list) == list:
        return True
    else:
        return False


print(sort([20, 50, 310, 60, 30]))
