import re
def read_file():
  with open('full_2_nline_body_for_hadoop.out','rb') as fin:
    for line in fin:
      print(len(re.findall('\B[A-Z]',line)))
            
def main():
    read_file()

if __name__ == "__main__":
    main()
