import sys, os, getopt

from utils import properties, sqlite


def main(argv):
    if not os.path.isdir("./.dat"):
        raise Exception("The current directory is not a dat project.")
    try:
        opts, args = getopt.getopt(argv, "hp:", ["help", "position="])
        if len(args) > 0:
            raise Exception("Unexpected arguments")
    except getopt.GetoptError:
        print('-p <position>')
        sys.exit(2)
        
    os.chdir("./.dat")
    
    last_page = properties.read_property('', 'lastPage')
    position = -1
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('-p <position>')
            sys.exit()
        elif opt in ("-p", "--position"):
            if int(arg) > last_page:
                raise Exception('The number of existing pages is ' + str(size) +
                      '. The position must be less or equal to ' + str(size))
            position = int(arg)
    
    if position == -1:
        raise Exception('The position of the page must be given. Check help for more information.')
    
    
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    
    sqlite.delete_row(cursor, 'pages', 'pageNum = {position}'.format(position=position))
    if position != last_page:
        command = sqlite.get_sql_command_from_file('decrease_subsequent_pages_position.sql')
        sqlite.execute_command(cursor, command.format(position = position))
    sqlite.close_connection(connection)
    properties.update_property('', "lastPage", last_page - 1)
    

if __name__ == "__main__":
    main(sys.argv[1:])
