import pika
from pika.adapters.blocking_connection import BlockingChannel


class CustomLogPublisher:
    """
    a custom log application that uses rabbitmq Fanout feature to make a Publisher/Subscriber Pattern
    For a message to Broadcast  to all worker nodes .
    it first declares an exchange then can be used to publish all messages and an async Consumer at last.
    """
    # TODO: Read from Config File
    EXCHANGE_TYPE = "fanout"
    EXCHANGE_NAME = "logs"

    def __init__(self, ):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def declare_exchange(self):
        self.channel.exchange_declare(exchange=self.EXCHANGE_NAME,
                                      exchange_type=self.EXCHANGE_TYPE)

    def notify_all(self, message):
        self.declare_exchange()
        self.channel.basic_publish(exchange=self.EXCHANGE_NAME, routing_key='', body=message)
        print(f"[*]published--->{message}")
