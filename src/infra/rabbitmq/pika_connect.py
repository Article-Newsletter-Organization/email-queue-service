import json
import pika
from pika.spec import Basic, BasicProperties
from pika.channel import Channel

from config.env import getEnvParams
from data.queue.message_body import MessageBody
from domain.services.interfaces.queue_consumer_allback import QueueConsumerCallback
from log.custom_logger import CustomLogger


class RabbitMQConsumer:
    logger = CustomLogger(name="RabbitMQConsumer")

    def __init__(self):
        self.envconfig = getEnvParams()["rabbit"]

        credentials = pika.PlainCredentials(
            self.envconfig["username"], self.envconfig["password"]
        )
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.envconfig["host"],
                port=self.envconfig["port"],
                credentials=credentials,
            )
        )
        self.channel = self.connection.channel()

        self.channel.exchange_declare(
            exchange=self.envconfig["exchange_name"], exchange_type="direct"
        )
        result = self.channel.queue_declare(queue=self.envconfig["queue_name"])

        self.queue_name = result.method.queue
        self.channel.queue_bind(
            exchange=self.envconfig["exchange_name"],
            queue=self.queue_name,
            routing_key=self.queue_name,
        )
        self.channel.basic_qos(prefetch_count=1)

    def consume(self, callback: QueueConsumerCallback):
        self._consumer = callback
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self._callback,
        )
        self.channel.start_consuming()

    def publish(self, message: MessageBody):
        json_data = json.dumps(message)

        self.channel.basic_publish(
            exchange=self.envconfig["exchange_name"],
            routing_key=self.queue_name,
            body=json_data,
            properties=BasicProperties(content_type="application/json"),
        )

    def _callback(
        self,
        ch: Channel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: str,
    ):
        self.logger.info("Callback initializing...")
        def record_result_callback(result: bool):
            if result is True:
                self.logger.info("Acknowledge positive.")
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                self.logger.info("Acknowledge negative.")
                ch.basic_nack(delivery_tag=method.delivery_tag)

        body_data = json.loads(body)

        self.logger.info("Connected with handler")

        self._consumer(
            MessageBody(**body_data),
            record_result_callback,
        )
