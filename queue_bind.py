import pika
from pika.adapters.blocking_connection import BlockingChannel


class QueueBind:
    def __init__(self, channel: BlockingChannel, queue_name: str, exchange_name: str, routing_key:str):
        self.channel = channel
        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self.channel.exchange_declare(self.exchange_name, "direct")
        self.channel.queue_declare(self.queue_name, False, True)
        self.channel.queue_bind(self.queue_name, self.exchange_name,  self.routing_key)

    def send_message(self, message):
        self.channel.basic_publish(self.exchange_name,  self.routing_key, message)

    def __repr__(self):
        return f"QueueBind(channel={self.channel}," \
               f"queue_name={self.queue_name})" \
               f"exchange_name={self.exchange_name})"