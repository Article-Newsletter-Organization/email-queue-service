import logging
import json

from models.log_model import LogModel
from errors.custom_error import CustomError
from models.metric_model import Metrics


class CustomFileFormatter(logging.Formatter):
    def format(self, record):
        customError: CustomError | None = getattr(record, "error", None)
        metrics: Metrics | None = getattr(record, "metrics", None)

        log_record = LogModel(
            name=getattr(record, "loggername", None),
            message=record.getMessage(),
            error=customError,
            level=record.levelname,
            metrics=metrics,
            metadata=getattr(record, "metadata", None),
        )

        return json.dumps(log_record.__dict__())
