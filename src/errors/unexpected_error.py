from errors.custom_error import CustomError


class UnexpectedError(CustomError):
    def __init__(
        self, message=None, traceback=None, issues=None, metadata: dict[str, str] = None
    ):
        super().__init__(
            message or "Ocorreu um erro inesperado!",
            traceback,
            self.__class__.__name__,
            issues,
            metadata,
        )
