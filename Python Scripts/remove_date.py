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
    i=0
    with open('date_gone_2.out','rb') as fin:
        with open('date_gone.out','w') as fout:
            for line in fin:
                i+=1
                if i is not 623:
                    row = line.split('\t')
                #row = row[:2] + row[3:]
                    fout.write('\t'.join(row))

def main():
    read_file()

if __name__ == "__main__":
    main()
