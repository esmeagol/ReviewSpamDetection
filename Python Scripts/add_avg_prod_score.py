import re
def read_file():
  i = 0
  diction = {}
  with open('new_avg_prod_ratings','r') as nfin:
    for line in nfin:
      prod, score = line.split('\t')
      diction[prod] = float(score)

  with open('new_with_avg_reviewer_rating.out','rb') as fin:
    with open('avg_ratings_caps_digits.out','wb') as fout:
      for line in fin:
        i+=1
        tabs = line.split('\t')
        cur_rating = float(tabs[5])
        try:
          avg_rating = diction[tabs[0]]
        except KeyError:
          print('cant find key ' + tabs[0])
          avg_rating = cur_rating
        tabs.append(str(avg_rating))
        tabs[11], tabs[12] = tabs[12], tabs[11]
        diff = abs(avg_rating-cur_rating)
        tabs.append(str(diff))
        tabs[12], tabs[13] = tabs[13], tabs[12]
        tabs.append(str(len(re.findall('\B[A-Z]', tabs[13]))))
        tabs.append(str(len(re.findall('[0-9]', tabs[13]))))
        tabs[13], tabs[15] = tabs[15], tabs[13]
        fout.write('\t'.join(tabs))
        #print('\t'.join(tabs))

def main():
    read_file()

if __name__ == "__main__":
    main()
