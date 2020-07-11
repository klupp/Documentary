import sys, os, getopt
import pandas as pd
import uuid

from pathlib import Path
from utils import sqlite

def main(argv):
    if not os.path.isdir("./.dat"):
        print("The current directory is not a dat project.")
    try:
        opts, args = getopt.getopt(argv, "hn:s:", ["help", "source=", "name="])
    except getopt.GetoptError:
        print('-s <source-path> -n <name>')
        sys.exit(2)
        
    os.chdir("./.dat")
    
    path = ''
    name = ''
    
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('<source-path> -n <name>')
            sys.exit()
        elif opt in ("-s", "--source"):
            path = arg
        elif opt in ("-n", "--name"):
            name = arg
            
    if path == '':
        print("You must specify a name for the data source that you want to load")
        print('-s <source> -n <name>')
        sys.exit(2)
        
    project_name = str(uuid.uuid4()) + ".csv"
    if name == '':
        name = Path(path).stem
    source_format = 'csv'
    
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    sqlite.insert_row(cursor, 'dataSources', ['sourcePath', 'projectPath', 'name', 'format'],
                      ['"{path}"'.format(path=path), '"{path}"'.format(path=project_name),
                       '"{name}"'.format(name=name), '"{var}"'.format(var=source_format)])
    sqlite.close_connection(connection)
    
    data = pd.read_csv(path)
    data.to_csv('datasources/' + project_name)


if __name__ == "__main__":
    main(sys.argv[1:])