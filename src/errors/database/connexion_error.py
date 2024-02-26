from errors.custom_error import CustomError


class ConnexionError(CustomError):
    def __init__(self, message=None, traceback=None, issues=None):
        super().__init__(
            message or "Ocorreu um erro ao tentar se conectar ao banco de dados!",
            traceback,
            self.__class__.__name__,
            issues,
        )
