import pika
from pika.adapters.blocking_connection import BlockingChannel
import json


class SyncConsumer:
    def __init__(self, channel: BlockingChannel, queue_name: str, exchange_name: str):
        self.channel = channel
        self.queue_name = queue_name
        self.exchange_name = exchange_name

    def _declare_queue(self):
        return self.channel.queue_declare(self.queue_name, durable=True)

    def _get_message_count(self):
        queue_state = self._declare_queue()
        return queue_state.method.message_count

    def get_messages(self):
        message_count = self._get_message_count()
        count = 0
        while count < message_count:
            method, properties, body = self.channel.basic_get(self.queue_name, auto_ack=True)
            print(json.loads(body))
            count += 1
