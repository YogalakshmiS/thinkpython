'''Exercise 10.12. Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list.'''




def reverse_pair(a):
    b=[]
    k=a+['Yoga']
    for x in a:
        c=''
        for i in range(len(x)):
            c=x[i]+c
        if list(c,k):
            b.append(x)
            k.remove(x)
            print (x)
        else: k.remove(x)
    return b
