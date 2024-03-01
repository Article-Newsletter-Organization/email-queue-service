from errors.custom_error import CustomError


class DatabaseError(CustomError):
    def __init__(
        self,
        message=None,
        traceback=None,
        issues=None,
        metadata: dict[str, str] = None,
    ):
        super().__init__(
            message
            or "Ocorreu um erro ao tentar executar uma query no banco de dados!",
            traceback,
            self.__class__.__name__,
            issues,
            metadata,
        )
