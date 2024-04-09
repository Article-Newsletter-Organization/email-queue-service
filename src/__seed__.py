from seed.postgres_seed import uploadSubscribers, uploadPublications
from seed.rabbitmq_seed import uploadRabbitMessages
from log.custom_logger import CustomLogger

import argparse

__logger__ = CustomLogger()


def main():
    parser = argparse.ArgumentParser(
        description="Script that adds data for testing in a development environment"
    )
    parser.add_argument(
        "--only-db",
        required=False,
        action="store_true",
        help="Only add data on the database",
    )
    parser.add_argument(
        "--only-queue",
        required=False,
        action="store_true",
        help="Only add data on the queue system",
    )

    args = parser.parse_args()

    if args.only_db:
        runDatabaseSeed()
    elif args.only_queue:
        runQueueSeed()
    else:
        runDatabaseSeed()
        runQueueSeed()


def runQueueSeed():
    __logger__.info("Migrating queue data...")

    uploadRabbitMessages()

    __logger__.info("Queue data migration completed!")


def runDatabaseSeed():
    __logger__.info("Migrating database data...")

    uploadSubscribers()
    uploadPublications()

    __logger__.info("Database data migration completed!")


main()
