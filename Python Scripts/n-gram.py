import csv
f = csv.reader(open('body.txt', 'r'), delimiter=' ')
i = 0
for line in f:
    i+=1
    # loop over words in input:
    #bigrams = {}
    #prev_word = 'BEGIN'
    #bigram = None
    #for word in line:
    #    bigram = prev_word + ' ' + word
    #    if bigram in bigrams:
    #        bigrams[bigram] += 1
    #    else:
    #        bigrams[bigram] = 1
    #    # change value of prev_word
    #    prev_word = word
    print(i)



