def read_file():
  i = 0
  with open('with_avg_prod_rating.out','rb') as fin:
    with open('full_2_nline_body_for_hadoop.out','wb') as fout:
      for line in fin:
        i += 1
        tabs = line.split('\t')
        body_str = tabs[11]
        body  = str(i) + ' ' + tabs[6] + tabs[11]
        fout.write(body)

def main():
    read_file()

if __name__ == "__main__":
    main()
