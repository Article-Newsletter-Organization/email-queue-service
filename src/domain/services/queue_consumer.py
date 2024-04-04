from infra.rabbitmq.pika_connect import RabbitMQConsumer
from .interfaces.queue_consumer_allback import QueueConsumerCallback

class QueueConsumer:
    def __init__(self):
        self._infra_consumer = RabbitMQConsumer()

    def consume(self, callback: QueueConsumerCallback):
        self._infra_consumer.consume(callback)
