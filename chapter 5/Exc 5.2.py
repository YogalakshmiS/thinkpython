def count(m):         
    if m < 0:
        print("Blastoff")
    elif m > 0:
        print(m)
        count(m - 1)

def arg(n,m):    
    for i in range(n):
        count(m)
    
arg(2, 8)
