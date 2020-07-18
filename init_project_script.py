from services.project_service import ProjectService

project_service = ProjectService()


def main():
    project_service.init_project()


if __name__ == "__main__":
    main()
