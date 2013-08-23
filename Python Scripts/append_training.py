def read_file():
  i = 0
  test = []
  with open('sample_text.txt','r') as fin:
      for line in fin:
          l = len(line)
          line = line[:l-1]
          test.append(line)

  with open('paa.txt','rb') as fin:
    with open('2_final.out','wb') as fout:
      for line in fin:
        tabs = line.split('\t')
        tabs.append(test[i])
        i+=1
        tabs[11], tabs[12] = tabs[12], tabs[11]
        fout.write('\t'.join(tabs))
      

def main():
    read_file()

if __name__ == "__main__":
    main()
