import os


def main(argv):
    path = argv[0] # get the path to the project from the arguments
    try:
        os.makedirs(path) # create directory where the dat project will be kept
    except FileExistsError:
        print("Directory " , dirName ,  " already exists. Choose another name")
    


if __name__ == "__main__":
    main(sys.argv[1:])
