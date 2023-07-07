class ApplicationError(Exception):
    pass


class UserExistError(ApplicationError):
    pass


class UserDataIncorrect(ApplicationError):
    pass
