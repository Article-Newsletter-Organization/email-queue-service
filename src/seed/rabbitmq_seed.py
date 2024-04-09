from pika import BasicProperties
from sqlalchemy import insert
import json
import os

from errors.unexpected_error import UnexpectedError
from infra.postgres.sqlalchemy_connect import SQLAlchemySession
from infra.postgres.sqlalchemy_models.subscribers import SubscriberAlchemyModel
from infra.postgres.sqlalchemy_models.publications import PublicationAlchemyModel
from infra.rabbitmq.pika_connect import RabbitMQConsumer
from log.custom_logger import CustomLogger

current_path = os.path.dirname(os.path.abspath(__file__))

queue_data_file = os.path.join(current_path, "data/rabbitmq_data.json")

consumer = RabbitMQConsumer()

logger = CustomLogger()


def uploadRabbitMessages():
    try:
        with open(queue_data_file, "r", encoding="utf-8") as file:
            message_list = json.load(file)
            for message in message_list:
                consumer.publish(
                    message,
                )
    except Exception as e:
        error = UnexpectedError(
            message="An error occurred while trying to insert data into the queue system",
            traceback=str(e),
        )

        raise error
