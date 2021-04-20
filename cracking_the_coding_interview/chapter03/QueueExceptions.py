class QueueException(Exception):
    """
    Queue Exception
    """
    pass

class QueueEmptyException(QueueException):

    def __init__(self):
        super().__init__("Queue Empty!")
