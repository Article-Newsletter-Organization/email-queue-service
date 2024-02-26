import psycopg2

from log.custom_logger import CustomLogger
from config.env import getEnvParams

from errors.database.connexion_error import ConnexionError


def database_connect():
    logger = CustomLogger("database_connect")
    config = getEnvParams()

    try:
        conn = psycopg2.connect(config["postgres"]["database_url"])

        logger.info("Database connected successfully.")

        return conn
    except Exception as e:
        error = ConnexionError(traceback=str(e))
        logger.error(error.message, error)
