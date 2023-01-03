from log_publisher import CustomLogPublisher


class DirectPublisher(CustomLogPublisher):
    EXCHANGE_NAME = 'directlogs'
    EXCHANGE_TYPE = 'direct'

    def __init__(self, routing_key):
        self.routing_key = routing_key
        super().__init__()

    def notify_all(self, message):
        self.declare_exchange()
        self.channel.basic_publish(exchange=self.EXCHANGE_NAME, routing_key=self.routing_key, body=message)
        print(f"[*]published {message} to routing_key = {self.routing_key}")
