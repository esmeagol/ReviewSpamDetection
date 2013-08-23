def read_file():
  with open('with_avg_prod_rating.out','rb') as fin:
    for line in fin:
      tabs = line.split('\t')
      pid = tabs[0]
      score = tabs[5]
      print('\t'.join([pid, score]))
            
def main():
    read_file()

if __name__ == "__main__":
    main()
