def read_file():
  ones = 0
  zeros = 0
  with open('training_data.out','rb') as fin:
    for line in fin:
      tabs = line.split('\t')
      score = int(tabs[8])
      if score is 1:
        ones += 1
      else:
        zeros += 1
    print(ones,zeros)
            
def main():
    read_file()

if __name__ == "__main__":
    main()
