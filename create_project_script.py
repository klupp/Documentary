import sys, os


def main(argv):
    path = argv[0] # get the path to the project from the arguments
    try:
        os.makedirs(path) # create directory where the dat project will be kept
        os.mkdir(path+"/.dat")
    except FileExistsError:
        print("Directory " , path ,  " already exists. Choose another name.")
    os.chdir(path)


if __name__ == "__main__":
    main(sys.argv[1:])
