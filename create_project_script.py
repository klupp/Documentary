import sys, os

from utils import sqlite, properties

def main(argv):
    if len(argv) > 1:
        raise Exception("Unexpected arguments")

    # create project folder
    path = argv[0] # get the path to the project from the arguments
    try:
        os.makedirs(path) # create directory where the dat project will be kept
        os.mkdir(path + "/.dat") # inside create the .dat folder
        os.mkdir(path + "/.dat/datasources") # create directory where the data sources will be kept
#         os.chdir(path + "/.dat") # change directory
    except FileExistsError:
        print("Directory " , path ,  " already exists. Choose another name.")
    
    path_project = path + '/.dat'
    path_here = os.path.dirname(os.path.realpath(__file__))
        
    # create tables
    conn = sqlite.open_connection(path_project + '/database.db')
    if conn:
        cursor = conn.cursor()
        commands = sqlite.get_sql_commands_from_file('create-tables.sql')
        sqlite.execute_commands(cursor, commands)
    sqlite.close_connection(conn)
        
    # create project properties
    print(path_project)
    properties.create_properties_file(path_project)


if __name__ == "__main__":
    main(sys.argv[1:])
