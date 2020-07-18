import os

from utils import sqlite, properties


class ProjectService:
    def __init__(self):
        pass

    def init_project(self):
        dat_project = './.dat'
        if os.path.isdir(dat_project):
            print("This is already a dat project.")
            return

        os.mkdir("./.dat")  # inside create the .dat folder
        os.chdir(dat_project)

        os.mkdir("./datasources")  # create directory where the data sources will be kept

        # create tables
        conn = sqlite.open_connection('./database.db')
        if conn:
            cursor = conn.cursor()
            commands = sqlite.get_sql_commands_from_file('create-tables.sql')
            sqlite.execute_commands(cursor, commands)
        sqlite.close_connection(conn)

        # create project properties
        properties.create_properties_file('./')

        print("DAT project created. Congratulations. Write `dat -h` for further usage info.")
