import os

from plac_core import ArgumentParser

from services.data_source_service import DataSourceService


parser = ArgumentParser()


def main(args):
    os.chdir("./.dat")
    data_source_service = DataSourceService()
    data_source_service.reload_all()


if __name__ == "__main__":
    main(parser.parse_args())
