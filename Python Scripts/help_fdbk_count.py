import csv
file = csv.reader(open('help_feedbacks.txt', 'r'))
max_f = 0
for row in file:
    if max_f < int(row[0]):
        max_f = int(row[0])

a=range(max_f+1)
b=[0]*(max_f+1)

file = csv.reader(open('help_feedbacks.txt', 'r'))
for row in file:
    b[int(row[0])] += 1

for i in range(max_f+1):
    if b[i] is not 0:
        print (a[i],b[i])
