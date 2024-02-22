import os


def getEnvParams() -> dict:
    return {
        "postgres": {
            "database_url": os.getenv("POSTGRES_DATABASE_URL"),
        },
        "rabbit": {
            "host": os.getenv("RABBIT_HOST"),
            "port": os.getenv("RABBIT_PORT"),
            "username": os.getenv("RABBIT_USERNAME"),
            "password": os.getenv("RABBIT_PASSWORD"),
            "queue_name": os.getenv("RABBIT_QUEUE_NAME"),
        },
        "app": {},
    }
