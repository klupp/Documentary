import sys, os, getopt

from utils import properties, sqlite

def main(argv):
    if not os.path.isdir("./.dat"):
        print("The current directory is not a dat project.")
    try:
        opts, args = getopt.getopt(argv, "hp:f:", ["help", "position=", "format="])
        if len(args) > 0:
            raise Exception("Unexpected arguments")
    except getopt.GetoptError:
        print('-p <position> -f <format>')
        sys.exit(2)
       
    # setup the current directory to be .dat
    os.chdir("./.dat")
    
    last_page = properties.read_property('', 'lastPage')
    position = last_page + 1
    page_format = "A4"
    
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('-p <position> -f <format>')
            sys.exit()
        elif opt in ("-p", "--position"):
            if int(arg) > (last_page + 1):
                raise Exception('The number of existing pages is ' + str(size) +
                      '. The position must be less or equal to ' + str(size + 1))
            position = int(arg)
        elif opt in ("-f", "--format"):
            page_format = arg
    
    connection = sqlite.open_connection('database.db')
    cursor = connection.cursor()
    if position != last_page + 1:
        command = sqlite.get_sql_command_from_file('update_subsequent_pages.sql')
        sqlite.execute_command(cursor, command.format(position = position))
    sqlite.insert_row(cursor, 'pages', ['format', 'pageNum'], ['"{var}"'.format(var=page_format), str(position)])
    sqlite.close_connection(connection)
    properties.update_property('', "lastPage", last_page + 1)
    
#     pages = pd.read_csv("pages.csv")
#     size = pages.shape[0]
#     position = size + 1
#     page_format = "A4"
#     
    
#     if position != (size + 1):
#         pages.loc[pages["pageNum"] >= position, "pageNum"] = pages.loc[pages["pageNum"] >= position, "pageNum"] + 1
#     pages.loc[size + 1] = [size + 1, page_format, position]
    
#     pages.to_csv("pages.csv", index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
