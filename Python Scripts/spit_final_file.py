import re
def read_file():
  with open('avg_ratings_caps_digits.out','rb') as fin:
    with open('final_for_regression.out','wb') as fout:
      i = 0
      for line in fin:
        i += 1
        tabs = line.split('\t')
        tabs.append(str(len(tabs[15].split())))
        tabs[15], tabs[16] = tabs[16], tabs[15]
        new_tabs = [str(i)] + tabs[3:6] + tabs[7:16]
        print('\t'.join(new_tabs))
        #print('\t'.join(tabs))

def main():
    read_file()

if __name__ == "__main__":
    main()
