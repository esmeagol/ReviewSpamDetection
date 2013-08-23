import csv
a=range(6)
b=[0]*(6)

file = csv.reader(open('ratings.txt', 'r'), delimiter='\t')
for row in file:
    b[int(row[0][0])] += 1

for i in range(6):
    if b[i] is not 0:
        print(a[i], b[i])
