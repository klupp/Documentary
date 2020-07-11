import os

from argparse import ArgumentParser

from utils import properties, sqlite
from utils.dat_project_decorator import dat_project

parser = ArgumentParser(description="Remove page from the `dat` project.")
parser.add_argument("-p", "--position", help="The position of the page to be removed.", type=int, required=True)


@dat_project
def main(position):
    os.chdir("./.dat")
    
    last_page = properties.read_property('', 'lastPage')

    if position > last_page:
        raise Exception('The number of existing pages is ' + str(last_page) +
                        '. The position must be less or equal to ' + str(last_page))
    
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    
    sqlite.delete_row(cursor, 'pages', 'pageNum = {position}'.format(position=position))
    if position != last_page:
        command = sqlite.get_sql_command_from_file('decrease_subsequent_pages_position.sql')
        sqlite.execute_command(cursor, command.format(position = position))
    sqlite.close_connection(connection)
    properties.update_property('', "lastPage", last_page - 1)
    

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.position)
