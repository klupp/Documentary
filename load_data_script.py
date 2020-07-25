import os
from argparse import ArgumentParser
from pathlib import Path

from services.data_source_service import DataSourceService
from utils.dat_project_decorator import dat_project
from utils.terminal_functions import update_terminal_question

parser = ArgumentParser(description="Add new datasource in your project")
parser.add_argument("path", help="path to the datasource file.", metavar="FILE")
parser.add_argument("-n", "--name", help="name the datasource (you will use this name later for reference). "
                                         "If name not provided the name of the file will be used.")
parser.add_argument('-u', '--update', action='store_true')


@dat_project
def load_data(path, req_name, update):
    os.chdir("./.dat")

    name = Path(path).stem

    if req_name is not None:
        name = req_name

    data_source_service = DataSourceService()
    data_source_service.load_datasource(path, name, update_terminal_question(update))


def main(args):
    load_data(args.path, args.name, args.update)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
