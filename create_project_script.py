import os
from argparse import ArgumentParser

from services.project_service import ProjectService

parser = ArgumentParser(description="Create new `dat` project")
parser.add_argument("path", help="path to the directory where the project will be created", metavar="DIR")

project_service = ProjectService()


def create_project(path):
    if not os.path.isdir(path):
        os.makedirs(path)  # create directory where the dat project will be kept
    os.chdir(path)

    project_service.init_project()


def main(args):
    create_project(args.path)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
