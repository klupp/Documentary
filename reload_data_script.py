import os

from services.data_source_service import DataSourceService


def main():
    os.chdir("./.dat")
    data_source_service = DataSourceService()
    data_source_service.reload_all()


if __name__ == "__main__":
    main()
