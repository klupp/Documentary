import sys, os, getopt
import pandas as pd
import uuid

from pathlib import Path
from utils import sqlite, properties

def main(argv):
    if not os.path.isdir("./.dat"):
        print("The current directory is not a dat project.")
    try:
        opts, args = getopt.getopt(argv, "hn:", ["help", "name="])
        if len(args) < 1:
            raise Exception("Please give the path to the source")
        if len(args) > 3:
            raise Exception("Unexpected arguments")
    except getopt.GetoptError:
        print('<source-path> -n <name>')
        sys.exit(2)
        
    os.chdir("./.dat")
        
    path = args[0]
    print(path)
    project_name = str(uuid.uuid4()) + ".csv"
    name = Path(path).stem
    source_format = 'csv'
    
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('<source-path> -n <name>')
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
            
    data = pd.read_csv(path)
    data.to_csv('datasources/' + project_name)
    
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    sqlite.insert_row(cursor, 'dataSources', ['sourcePath', 'projectPath', 'name', 'format'],
                      ['"{path}"'.format(path=path), '"{path}"'.format(path=project_name),
                       '"{name}"'.format(name=name), '"{var}"'.format(var=source_format)])
    sqlite.close_connection(connection)


if __name__ == "__main__":
    main(sys.argv[1:])