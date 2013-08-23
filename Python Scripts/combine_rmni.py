import csv

def combine_tabs():
    f = csv.reader(open('data1.out', 'r'), delimiter='\t')
    #new_1 = csv.writer(open('new_1.txt','w'), delimiter='\t')
    #i = 0
    #for row in fe:
    #    print i
    #    i+=1
    #    new_1.writerow(row)
    for row in f:
        if row:
            l = len(row)
            if l > 8:
                print(' '.join(row[8:l]))
            

def read_file():
    i = 0
    diff = []
    with open('sample_text.txt', 'r') as newf:
        for line in newf:
            l = len(line)
            diff.append(line[:l-2])
    with open('reviewsNew.txt','rb') as fin:
        with open('data1.out','w') as fout:
            for line in fin:
                if i is not 138:
                    fout.write('\t'.join(line.split('\t')))
                i+=1

def main():
    read_file()

if __name__ == "__main__":
    main()
