import sys, os, getopt
import pandas as pd


def main(argv):
    if not os.path.isdir("./.dat"):
        print("The current directory is not a dat project.")
    try:
        opts, args = getopt.getopt(argv, "hp:f:", ["position=", "format="])
    except getopt.GetoptError:
        print('-p <position> -f <format>')
        sys.exit(2)
        
    os.chdir("./.dat")
    pages = pd.read_csv("pages.csv")
    size = pages.shape[0]
    position = size + 1
    page_format = "A4"
    for opt, arg in opts:
        if opt == '-h':
            print('-p <position> -f <format>')
            sys.exit()
        elif opt in ("-p", "--position"):
            if int(arg) > (size + 1):
                raise Exception('The number of existing pages is ' + str(size) +
                      '. The position must be less or equal to ' + str(size + 1))
            position = int(arg)
        elif opt in ("-f", "--format"):
            page_format = arg
    
    if position != (size + 1):
        pages.loc[pages["pageNum"] >= position, "pageNum"] = pages.loc[pages["pageNum"] >= position, "pageNum"] + 1
    pages.loc[size + 1] = [size + 1, page_format, position]
    
    pages.to_csv("pages.csv", index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
