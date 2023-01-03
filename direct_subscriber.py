from log_subscriber import CustomLogSubscriber


class DirectLogSubscriber(CustomLogSubscriber):
    """
    extends CustomLogSubscriber .
    usage of this class is Routing(Binding) Key Consuming Of Messages .
    """
    # TODO: read from Config File
    EXCHANGE_NAME = 'logs'
    EXCHANGE_TYPE = 'direct'

    def __init__(self, routing_key):
        self.routing_key = routing_key
        super().__init__()

    def _bind_exchange_and_queue(self):
        self.channel.queue_bind(exchange=self.EXCHANGE_NAME, queue=self.queue_name,
                                routing_key=self.routing_key)
