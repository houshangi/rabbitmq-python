import pika


class CustomLogSubscriber:
    EXCHANGE_NAME = 'logs'

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self._create_temp_queue()
        self._bind_exchange_and_queue()

    def _create_temp_queue(self):
        self.temp_queue = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = self.temp_queue.method.queue

    def _bind_exchange_and_queue(self):
        self.channel.queue_bind(exchange=self.EXCHANGE_NAME, queue=self.queue_name)

    def subscribe(self):
        def callback(ch, method, properties, body):
            print(f"[*]recieved {body}")

        self.channel.basic_consume(
                queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        print(f"[*]Reciving messages to quit press Ctrl+C")
        self.channel.start_consuming()

