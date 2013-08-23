def read_file():
  i = 0
  diction = {}
  with open('avg_prod_rating_output','r') as nfin:
    for line in nfin:
      prod, score = line.split('\t')
      l = len(score)
      score = score[:l-1]
      #print( prod, score)
      diction[prod] = score

  with open('with_avg_prod_rating.out','rb') as fin:
    with open('new_with_avg_prod_rating.out','wb') as fout:
      for line in fin:
        i+=1
        tabs = line.split('\t')
        cur_rating = tabs[5]
        try:
          avg_rating = diction[tabs[1]]
        except KeyError:
          print(tabs[0], ' key error')
          avg_rating = cur_rating
        tabs[9] = avg_rating
        diff = abs(float(avg_rating)-float(cur_rating))
        tabs[10] = str(diff)
        fout.write('\t'.join(tabs))

def main():
    read_file()

if __name__ == "__main__":
    main()
