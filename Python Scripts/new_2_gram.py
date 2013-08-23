f = 'body.txt'
fl = open(f,'r')
line = fl.readline()
lst_grams = []
#while line:
i = 0
while i < 150000:
    i += 1
    a = frozenset(line.split())
    lst_grams.append(a)
    line = fl.readline()
fl.close()

i = 0
for a in lst_grams:
    i+=1
    for b in lst_grams[i:]:
        similarity = float(len(a.intersection(b))*1.0/len(a.union(b)))
        if similarity > 0.5:
            print(lst_grams.index(a), lst_grams.index(b), similarity)
