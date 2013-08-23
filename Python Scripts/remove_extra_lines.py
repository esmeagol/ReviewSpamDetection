def read_file():
  with open('final.out','rb') as fin:
    with open('new_final.out', 'w') as fout:
      for line in fin:
        tabs = line.split('\t')
        l = len(tabs)
        if l is 13:
            fout.write('\t'.join(tabs))

def main():
    read_file()

if __name__ == "__main__":
    main()
