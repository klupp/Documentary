import sys, os, getopt
import pandas as pd
import uuid
from argparse import ArgumentParser

from pathlib import Path
from utils import sqlite, properties
from utils.dat_project_decorator import dat_project

parser = ArgumentParser(description="Create new `dat` project")
parser.add_argument("path", help="path to the datasource file.", metavar="FILE")
parser.add_argument("-n", "--name", help="name the datasource (you will use this name later for reference). "
                                         "If name not provided the name of the file will be used.")


@dat_project
def main(path, req_name):
        
    os.chdir("./.dat")

    project_name = str(uuid.uuid4()) + ".csv"
    name = Path(path).stem
    source_format = 'csv'
    
    if req_name is not None:
        name = req_name
    
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    sqlite.insert_row(cursor, 'dataSources', ['sourcePath', 'projectPath', 'name', 'format'],
                      ['"{path}"'.format(path=path), '"{path}"'.format(path=project_name),
                       '"{name}"'.format(name=name), '"{var}"'.format(var=source_format)])
    sqlite.close_connection(connection)

    data = pd.read_csv(path)
    data.to_csv('datasources/' + project_name)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.path, args.name)
