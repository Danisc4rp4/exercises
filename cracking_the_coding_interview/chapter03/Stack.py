from StackExceptions import StackEmptyException


class Stack(object):

    class StackNode():

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def pop(self):
        if not self.top:
            raise StackEmptyException()
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        newNode = self.StackNode(data)
        newNode.next = self.top
        self.top = newNode

    def peek(self):
        if not self.top:
            raise StackEmptyException()
        return self.top.data

    def isEmpty(self):
        return not self.top