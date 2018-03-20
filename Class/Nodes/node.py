"""This module contains class objects required for linked lists"""


class Node(object):
    """This creates a node object with a next node pointer"""

    def __init__(self, val, prev=None, next=None):
        """Default constructor. Only requires a value"""
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"This is a Node: {self.val}"


class LinkedList(object):
    start = None
    end = None

    def __init__(self):
        self.start = None
        self.end = None

    def __str__(self):
        # return f"This is a LinkedList"
        name = "This is a list: {"
        node = self.start
        while node is not None:
            name += f" {node.val}"
            node = node.next
            if node is not None:
                name += ","
        name += " }"
        return name

    def add(self, val):
        if (self.start is None):
            self.start = Node(val)
            self.end = self.start
        else:
            self.end.next = Node(val)
            self.end = self.end.next


class Restaurant(object):
    bankrupt = False

    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")


if __name__ == "__main__":
    n1 = Node(25)
    print(n1)
    l1 = LinkedList()
    l1.add(1)
    l1.add(2)
    l1.add(3)
    print(l1)
