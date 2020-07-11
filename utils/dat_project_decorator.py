import os


def dat_project(func):
    def wrapper(*args, **kwargs):
        if not os.path.isdir("./.dat"):
            raise AssertionError("`dat` is not initialized. Please either call `dat init` to initialize this project"
                                 " or `dat create <path>` to create new project.")
        func(*args, *kwargs)

    return wrapper
