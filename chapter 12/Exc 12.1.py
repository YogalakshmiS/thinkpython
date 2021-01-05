'''Exercise 12.3. Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages.'''






word = 'Every challenge creates an opportunity'


def order_freq(x):
    dicts = {}
    for let in x:
        dicts[let] = 1 + dicts.get(let, 0)
    return dicts


def most_frequent(word):
    lets = [let.lower() for let in word if let.isalpha()]
    dicts = order_freq(lets)
    result = []
    for key in dicts:
        result.append((dicts[key], key))
    result.sort(reverse=True)
    for count, let in result:
        print (let, count)

most_frequent(word)
