import sys, os, getopt
import pandas as pd


def main(argv):
    if not os.path.isdir("./.dat"):
        raise Exception("The current directory is not a dat project.")
    try:
        opts, args = getopt.getopt(argv, "hp:", ["help", "position="])
        if len(args) > 0:
            raise Exception("Unexpected arguments")
    except getopt.GetoptError:
        print('-p <position>')
        sys.exit(2)
        
    os.chdir("./.dat")
    pages = pd.read_csv("pages.csv")
    size = pages.shape[0]
    position = -1
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('-p <position>')
            sys.exit()
        elif opt in ("-p", "--position"):
            if int(arg) > size:
                raise Exception('The number of existing pages is ' + str(size) +
                      '. The position must be less or equal to ' + str(size))
            position = int(arg)
    
    if position == -1:
        raise Exception('The position of the page must be given. Check help for more information.')
    
    pages.drop(index=pages.index[pages["pageNum"]==position], inplace=True)
    if position != (size + 1):
        pages.loc[pages["pageNum"] > position, "pageNum"] = pages.loc[pages["pageNum"] >= position, "pageNum"] - 1
    
    pages.to_csv("pages.csv", index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
