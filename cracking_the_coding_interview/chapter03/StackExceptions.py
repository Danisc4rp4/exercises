class StackException(Exception):
    """
    Stack Exception
    """
    pass

class StackEmptyException(StackException):

    def __init__(self):
        super().__init__("Stack Empty!")
