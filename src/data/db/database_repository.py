from abc import ABC

from log.custom_logger import CustomLogger


class DatabaseRepository(ABC):
    logger = CustomLogger("DatabaseRepository")

    def __init__(self):
        self.logger.info("DatabaseRepository initialized successfully.")

    def __finish__(self):
        self.logger.info("Database clossing connection...")
        self.logger.info("Database connection closed!")
