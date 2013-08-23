def read_file():
  i = 0
  test = {}
  with open('product_info.txt','rb') as fin:
    for line in fin:
      tabs = line.split('\t')
      print tabs

  with open('full_2_nline_hadoop_body.out','rb') as fin:
      for line in fin:
          line = line[:l-1]


def main():
    read_file()

if __name__ == "__main__":
    main()
