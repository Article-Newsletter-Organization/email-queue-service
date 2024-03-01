from abc import ABC

from infra.postgres.psycopg2_connect import database_connect
from log.custom_logger import CustomLogger


class DatabaseRepository(ABC):
    logger = CustomLogger("DatabaseRepository")

    def __init__(self):
        self.conn = database_connect()
        self.cursor = self.conn.cursor()
        self.logger.info("DatabaseRepository initialized successfully.")

    def __finish__(self):
        self.logger.info("Database clossing connection...")
        self.cursor.close()
        self.conn.close()
        self.logger.info("Database connection closed!")
