from typing import Callable, TypeAlias
from data.queue.message_body import MessageBody


QueueConsumerCallback: TypeAlias = Callable[[MessageBody, Callable[[bool], None]], None]
