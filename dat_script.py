from argparse import ArgumentParser
import create_project_script
import init_project_script
import create_page_script
import load_data_script
import reload_data_script
import remove_page_script


parser = ArgumentParser()
subparsers = parser.add_subparsers(title="Commands",
                                   description="List of all available `dat` commands.", dest="command")
create = subparsers.add_parser('create', parents=[create_project_script.parser], add_help=False)
init = subparsers.add_parser('init', parents=[init_project_script.parser], add_help=False)
refresh = subparsers.add_parser('refresh', parents=[reload_data_script.parser], add_help=False)

add = subparsers.add_parser("add")
add_subparsers = add.add_subparsers(title="Add commands",
                                    description="List of all available `dat add` commands.", dest="add_command")
add_subparsers.add_parser("page", parents=[create_page_script.parser], add_help=False)
add_subparsers.add_parser("data", parents=[load_data_script.parser], add_help=False)

remove = subparsers.add_parser("remove")
remove_subparsers = remove.add_subparsers(title='Remove commands',
                                          description="List of all available `dat remove` commands.", dest="remove_command")
remove_subparsers.add_parser("page", parents=[remove_page_script.parser], add_help=False)


def add_command(args):
    switcher = {
        "page": create_page_script.main,
        "data": load_data_script.main
    }
    switcher.get(args.add_command)(args)


def remove_command(args):
    switcher = {
        "page": remove_page_script.main
    }
    switcher.get(args.remove_command)(args)


def main(args):
    switcher = {
        "create": create_project_script.main,
        "init": init_project_script.main,
        "add": add_command,
        "remove": remove_command,
        "refresh": reload_data_script.main
    }

    switcher.get(args.command)(args)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
