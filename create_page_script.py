import os

from argparse import ArgumentParser

from utils import properties, sqlite
from utils.dat_project_decorator import dat_project

parser = ArgumentParser(description="Create new page in the `dat` project.")
parser.add_argument("-p", "--position", help="Position on which the page will be added.", type=int)
parser.add_argument("-f", "--format", help="Format of the page.", choices=['A4'], default='A4')


@dat_project
def create_page(req_position, page_format):
    # setup the current directory to be .dat
    os.chdir("./.dat")

    last_page = properties.read_property('', 'lastPage')
    if req_position is None:
        position = last_page + 1
    else:
        if req_position > (last_page + 1):
            raise Exception('The number of existing pages is ' + str(last_page) +
                            '. The position must be less or equal to ' + str(last_page + 1))
        position = req_position

    print(position, page_format)
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    if position != last_page + 1:
        command = sqlite.get_sql_command_from_file('increase_subsequent_pages_position.sql')
        sqlite.execute_command(cursor, command.format(position = position))
    sqlite.insert_row(cursor, 'pages', ['format', 'pageNum'], ['"{var}"'.format(var=page_format), str(position)])
    sqlite.close_connection(connection)
    properties.update_property('', "lastPage", last_page + 1)


def main(args):
    create_page(args.position, args.format)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
