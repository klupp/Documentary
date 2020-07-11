import sys, os, getopt
import pandas as pd

from utils import sqlite

def main(argv):
    if not os.path.isdir("./.dat"):
        print("The current directory is not a dat project.")
    try:
        opts, args = getopt.getopt(argv, "hn:s:", ["help", "name=", "source="])
    except getopt.GetoptError:
        print('-n <name> -s <source>')
        sys.exit(2)
        
    os.chdir("./.dat")
        
    name = ''
    source = ''
    
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('-n <name> -s <source>')
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-s", "--source"):
            source = arg
            
    
    if name == '':
        print("You must specify a name for the data source that you want to reload")
        print('-n <name> -s <source>')
        sys.exit(2)
                  
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    rows = sqlite.select_rows(cursor, 'dataSources', 'name = "{name}"'.format(name=name))
                  
    if len(rows) < 1:
        print("Does not exist a data source for the given name: " + name)
        sys.exit(2)
                  
    row = rows[0]
    if source == '':
        source = row['sourcePath']
        
    sqlite.update_row(cursor, 'dataSources', ['sourcePath'],
                      ['"{path}"'.format(path=source)], 'name = "{name}"'.format(name=name))
    sqlite.close_connection(connection)
                  
    data = pd.read_csv(source)
    data.to_csv('datasources/' + row['projectPath'])


if __name__ == "__main__":
    main(sys.argv[1:])