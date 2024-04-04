from errors.custom_error import CustomError


class EmailSendError(CustomError):
    def __init__(
        self,
        message: str = None,
        traceback=None,
        issues=None,
        metadata: dict[str, str] = None,
    ):
        super().__init__(
            message or "Ocorreu um erro ao enviar e-mail!",
            traceback,
            self.__class__.__name__,
            issues,
            metadata,
        )
