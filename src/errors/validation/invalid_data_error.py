from errors.custom_error import CustomError


class InvalidDataError(CustomError):
    def __init__(self, message=None, traceback=None, issues=None):
        super().__init__(
            message or "Ocorreu um erro na validação dos dados!",
            traceback,
            self.__class__.__name__,
            issues,
        )
