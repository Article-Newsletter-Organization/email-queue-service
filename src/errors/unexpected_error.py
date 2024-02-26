from errors.custom_error import CustomError


class UnexpectedError(CustomError):
    def __init__(self, message=None, trace=""):
        super().__init__(
            message or "Ocorreu um erro inesperado!", trace, self.__class__.__name__
        )
