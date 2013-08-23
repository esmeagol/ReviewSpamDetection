def read_file():
  with open('with_training.out','rb') as fin:
    with open('training_data.out','w') as fout1:
      with open('test_data.out','w') as fout2:
        for line in fin:
          tabs = line.split('\t')
          score = int(tabs[8])
          if score is 2:
            fout2.write('\t'.join(tabs))
          else:
            fout1.write('\t'.join(tabs))
            
def main():
    read_file()

if __name__ == "__main__":
    main()
