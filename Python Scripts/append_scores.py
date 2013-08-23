def read_file():
  i = 0
  diction = {}
  with open('avg-score-output','r') as nfin:
    for line in nfin:
      member, score = line.split('\t')
      diction[member] = float(score)

  with open('only_8_tabs.out','rb') as fin:
    with open('with_scores.out','w') as fout:
      for line in fin:
        i+=1
        tabs = line.split('\t')
        tabs.append(str(diction[tabs[1]]))
        tabs[7], tabs[8] = tabs[8], tabs[7]
        fout.write('\t'.join(tabs))
        #print('\t'.join(tabs))

def main():
    read_file()

if __name__ == "__main__":
    main()
