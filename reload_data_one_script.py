import sys, os, getopt
import pandas as pd

from argparse import ArgumentParser
from utils import sqlite
from utils.dat_project_decorator import dat_project

parser = ArgumentParser(description="Create new `dat` project")
parser.add_argument("-n", "--name", help="Name of the data we want to reload.", required=True)
parser.add_argument("-s", "--source", help="Source where the data should be read from")


@dat_project
def main(name, source):
    os.chdir("./.dat")
        
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    rows = sqlite.select_rows(cursor, 'dataSources', 'name = "{name}"'.format(name=name))
                  
    if len(rows) < 1:
        print("Does not exist a data source for the given name: " + name)
        sys.exit(2)
                  
    row = rows[0]
    if source != None:
        sqlite.update_row(cursor, 'dataSources', ['sourcePath'],
                      ['"{path}"'.format(path=source)], 'name = "{name}"'.format(name=name))
    else:
        source = row['sourcePath']
        
    sqlite.close_connection(connection)
    
    data = pd.read_csv(source)
    data.to_csv('datasources/' + row['projectPath'])


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.name, args.source)