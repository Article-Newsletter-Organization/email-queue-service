import os
from dotenv import load_dotenv, find_dotenv


def getEnvParams() -> dict:
    load_dotenv(dotenv_path=find_dotenv(), override=True)

    return {
        "smtp": {
            "username": os.getenv("SMTP_USERNAME"),
            "password": os.getenv("SMTP_PASSWORD"),
            "email": os.getenv("SMTP_EMAIL"),
            "server": os.getenv("SMTP_SERVER"),
            "port": os.getenv("SMTP_PORT"),
        },
        "postgres": {
            "database_url": os.getenv("POSTGRES_DATABASE_URL"),
        },
        "rabbit": {
            "host": os.getenv("RABBIT_HOST"),
            "port": os.getenv("RABBIT_PORT"),
            "username": os.getenv("RABBIT_USERNAME"),
            "password": os.getenv("RABBIT_PASSWORD"),
            "exchange_name": os.getenv("RABBIT_EXCHANGE_NAME"),
            "queue_name": os.getenv("RABBIT_QUEUE_NAME"),
        },
        "app": {},
    }
