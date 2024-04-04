import json
import pika
from pika.spec import Basic, BasicProperties

from config.env import getEnvParams
from data.queue.message_body import MessageBody
from domain.services.interfaces.queue_consumer_allback import QueueConsumerCallback


class RabbitMQConsumer:
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
            exchange=self.envconfig["topic_name"], exchange_type="fanout"
        )
        result = self.channel.queue_declare(queue="", exclusive=True)

        self.queue_name = result.method.queue
        self.channel.queue_bind(
            exchange=self.envconfig["topic_name"],
            queue=self.queue_name,
        )
        self.channel.basic_qos(prefetch_count=1)

    def consume(self, callback: QueueConsumerCallback):
        self._consumer = callback
        self.channel.basic_consume(
            queue=self.envconfig["topic_name"],
            on_message_callback=self._callback,
        )

    def _callback(
        self,
        ch,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: str,
    ):
        print(f"METHOD: \n${vars(method)}")
        print(f"PROPERTIES: \n${vars(properties)}")
        print(f"BODY: \n${body}")

        def record_result_callback(result: bool):
            if result is True:
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                ch.basic_nack(delivery_tag=method.delivery_tag)

        body_data = json.dump(body)
        print(body_data)

        self._consumer(
            MessageBody(
                "raiogjaor",
                "okfoewijgoaiwga",
                "Subject",
                "Body cool",
                "https://google.com.br",
                "ajeroiggkaorei",
            ),
            record_result_callback,
        )
