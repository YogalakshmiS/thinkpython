'''. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What set of 8 letters forms the most possible bingos?'''

anagrams="yoga"


def find_bingos(anagrams):
    
    candi = [anagrams[key] for key in anagrams if len(key) == 8]
    candi.sort(key=len, reverse=True)

    print ("Top Bingos:")
    for i in range(0, 2):
        k = ''.join(sorted(candi[i][0]))
        print ("%s) %d: %s" % ((i + 1), len(candi[i]), fp), candi[i])

  
    print ("\n")

find_bingos(anagrams)
