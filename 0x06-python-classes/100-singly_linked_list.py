#!/usr/bin/python3
"""Singly linked list"""
class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialize class instance"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set value for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of the next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initialization"""
        self.__head = None

    def sorted_insert(self, value):
        """Represents a sorted singly linked list."""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout: one node number by line"""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
