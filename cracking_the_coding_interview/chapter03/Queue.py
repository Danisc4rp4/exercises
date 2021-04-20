from QueueExceptions import QueueEmptyException

class Queue(object):

    class QueueNode():

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        newNode = self.QueueNode(data)
        if self.last:
            self.last.next = newNode
        self.last = newNode
        if not self.first:
            self.first = self.last

    def remove(self):
        if not self.first:
            raise QueueEmptyException
        data = self.first.data
        self.first = self.first.next
        return data

    def peek(self):
        if not self.first:
            raise QueueEmptyException()
        return self.first.data

    def isEmpty(self):
        return not self.first