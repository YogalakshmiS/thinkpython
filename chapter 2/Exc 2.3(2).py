'''
2.   Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?

'''



price = 24.95
disc = 40/100
cost_for_fbook = 3
cost_for_addbooks = 0.75
tot_books = 60
discount_for_singlebook = price*disc
discount_book_price = price - discount_for_singlebook
shipping_cost = shipping_cost_for_addbooks*(total_books-1)+cost_for_fbook
total_wholesale= discounted_book_price*60 + shipping_cost
print(total_wholesale)