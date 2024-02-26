import logging
from pythonjsonlogger import jsonlogger

from models.metric_model import Metrics
from errors.custom_error import CustomError
from log.file_formatter import CustomFileFormatter


GLOBAL_LOGGER_NAME = "GLOBAL"


class CustomLogger:
    _instance = None

    def __new__(cls, name=GLOBAL_LOGGER_NAME):
        cls.loggername = name

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.setup_logger()

        return cls._instance

    def setup_logger(self):
        logger = logging.getLogger(self.loggername)
        logger.setLevel(logging.INFO)

        formatter = CustomFileFormatter()
        file_handler = logging.FileHandler("output.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s: %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        self.logger = logger

    def info(self, message: str, metrics: Metrics = None, metadata: dict = None):
        self.logger.info(
            message,
            extra={"metrics": metrics, "metadata": metadata, "loggername": self.loggername},
        )

    def error(
        self,
        message: str,
        error: CustomError = None,
        metrics: Metrics = None,
        metadata: dict = None,
    ):
        self.logger.error(
            message,
            extra={
                "error": error,
                "metrics": metrics,
                "metadata": metadata,
                "loggername": self.loggername,
            },
        )

    def warn(self, message: str, metrics: Metrics = None, metadata: dict = None):
        self.logger.warn(
            message,
            extra={"metrics": metrics, "metadata": metadata, "loggername": self.loggername},
        )
