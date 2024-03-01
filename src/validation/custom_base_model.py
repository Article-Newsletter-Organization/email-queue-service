from pydantic import BaseModel, ValidationError

from log.custom_logger import CustomLogger
from errors.validation.invalid_data_error import InvalidDataError


class CustomBaseModel(BaseModel):
    @classmethod
    def model_validate(cls, obj):
        logger = CustomLogger()

        try:
            return super().model_validate(obj)
        except ValidationError as e:
            error = InvalidDataError(traceback=str(e))
            logger.error(error.message, error)

            raise error
