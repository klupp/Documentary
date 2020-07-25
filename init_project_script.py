from plac_core import ArgumentParser

from services.project_service import ProjectService

project_service = ProjectService()


parser = ArgumentParser()


def init_project():
    project_service.init_project()


def main(args):
    init_project()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
