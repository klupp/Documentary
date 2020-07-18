import sys
import uuid

import pandas as pd

from utils import sqlite

from colorama import init, Fore, Style


class DataSourceService:
    def __init__(self):
        pass

    def reload_all(self):
        init()

        connection = sqlite.open_connection('database.db')
        cursor = connection.cursor()
        rows = sqlite.select_rows(cursor, 'dataSources')

        for index, row in enumerate(rows):
            source = row['sourcePath']
            try:
                data = pd.read_csv(source)
                data.to_csv('datasources/' + row['projectPath'])
                print(Fore.GREEN + str(index + 1), row['name'] + ":", source, "reloaded.", Style.RESET_ALL)
            except FileNotFoundError as e:
                print(Fore.YELLOW + str(index + 1), row['name'] + ":",
                      source, "not found. Please fix the `source path` using the `name` as key.", Style.RESET_ALL,
                      file=sys.stderr)
                continue

        sqlite.close_connection(connection)

    def load_datasource(self, path, name, update):
        connection = sqlite.open_connection('database.db')
        cursor = connection.cursor()
        rows = sqlite.select_rows(cursor, 'dataSources', 'name = "{name}"'.format(name=name))

        if len(rows) == 1:
            row = rows[0]
            project_name = row['projectPath']
            if row['sourcePath'] != path and update("Do you want to update the source path?"):
                sqlite.update_row(cursor, 'dataSources', ['sourcePath'],
                                  ['"{path}"'.format(path=path)], 'name = "{name}"'.format(name=name))
                print("Source path successfully updated to:", path, "for:", name)
            else:
                return
        else:
            project_name = str(uuid.uuid4()) + ".csv"
            source_format = 'csv'
            sqlite.insert_row(cursor, 'dataSources', ['sourcePath', 'projectPath', 'name', 'format'],
                              ['"{path}"'.format(path=path), '"{path}"'.format(path=project_name),
                               '"{name}"'.format(name=name), '"{var}"'.format(var=source_format)])
            print("New data source successfully added with pat:", path, "for:", name)

        sqlite.close_connection(connection)

        try:
            data = pd.read_csv(path)
            data.to_csv('datasources/' + project_name)
            print(name + ":", path, "successfully loaded.")
        except FileNotFoundError as e:
            print(Fore.YELLOW + name + ":",
                  path, "not found. Please fix the `source path` using the `name` as key.", Style.RESET_ALL,
                  file=sys.stderr)