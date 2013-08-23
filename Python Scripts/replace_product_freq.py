from nltk.stem.wordnet import WordNetLemmatizer

def replace_prod_freq():
    diction = {}
    with open('product_freq.txt', 'r') as freq:
        i = 0
        for line in freq:
            row = line.split('\t')
            i += 1
            if len(row) is 1:
                print i
            diction[row[0]]=row[1]


    with open('date_gone.out', 'rb') as fin:
        with open('with_prod_freq.out', 'w') as fout:
            for line in fin:
                row = line.split('\t')
                row = row + diction.get(row[0])
                fout.write('\t'.join(row))


def stemming():
    lmtzr = WordNetLemmatizer()
    with open('date_gone.out', 'rb') as fin:
        with open('stemmed.out', 'w') as fout:
            i = 0
            for line in fin:
                #i+=1
                new_data = []
                row = line.split('\t')
                #print(i)
                l = len(row)
                if l > 5:
                    data = row[5]
                    words = data.split(' ')
                    for word in words:
                        new_word = lmtzr.lemmatize(word)
                        new_data.append(new_word)
                    row[5] = ' '.join(new_data)
                if l > 6:
                    data = row[6]
                    words = data.split(' ')
                    for word in words:
                        new_word = lmtzr.lemmatize(word)
                        new_data.append(new_word)
                    row[6] = ' '.join(new_data)
                fout.write('\t'.join(row))

def main():
    stemming()

if __name__ == "__main__":
    main()
