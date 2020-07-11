import os
import sqlite3


path = os.path.dirname(os.path.realpath(__file__)) + '/../sqls/'


def get_sql_commands_from_file(file_name):
    file = open(path + file_name, 'r').read()
    sql_commands = file.split(';')
    return sql_commands


def get_sql_command_from_file(file_name):
    return open(path + file_name, 'r').read()


def open_connection(path):
    try:
        connection = sqlite3.connect(path)
        connection.row_factory = dict_factory
        return connection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite:", error)


def close_connection(connection):
    if connection:
        connection.commit()
        connection.close()
        

def execute_commands(cursor, commands):
    for command in commands:
        execute_command(cursor, command)
            

def execute_command(cursor, command):
    try:
        cursor.execute(command)
    except sqlite3.OperationalError as error:
        print("Command skipped: ", error)
        
        
def insert_row(cursor, table, columns, values):
    command = """INSERT INTO {table} ({columns}) VALUES ({values});""".format(
        table=table, columns=', '.join(columns), values=', '.join(values))
    print(command)
    execute_command(cursor, command)
    
    
def update_row(cursor, table, columns, values, condition):
    if len(columns) != len(values):
        raise Exception("For every column there should be a respective value.")
    
    command = """UPDATE {table} SET {setup} WHERE {condition};""".format(
        table=table,
        setup=', '.join([columns[idx] + " = " + values[idx] for idx in range(len(columns))]),
        condition=condition)
    print(command)
    execute_command(cursor, command)
    
    
def delete_row(cursor, table, condition):
    command = """DELETE FROM {table} WHERE {condition};""".format(
        table=table, condition=condition)
    print(command)
    execute_command(cursor, command)
    

def select_rows(cursor, table, condition):
    command = """SELECT * FROM {table} WHERE {condition};""".format(
        table=table, condition=condition)
    print(command)
    execute_command(cursor, command)
    rows = cursor.fetchall()
    return rows


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d