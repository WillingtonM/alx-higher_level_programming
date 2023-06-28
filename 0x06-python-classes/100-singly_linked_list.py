#!/usr/bin/python3
""" Define classes for singly linked lsit."""

class Node:
    """Node class in linked list."""

    def __init__(self, data, next_node=None):
        """Intialize new Node class.

        Args:
           data (int): Data of new Node.
           next_node (Node): Next node of new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data of node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next_node of node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Define SinglyLinkedList class object."""

class SinglyLinkedList:
    """SinglyLinkedList in linked list."""

    def __str__(self):
        """Define print() representation of linked list."""
        ret = []
        tmp = self.__head
        while tmp is not None:
            ret.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(ret))

    def __init__(self):
        """Initialize new Linked list class."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node to linked list.

        Args:
           value (Node): New Node to insert.
        """
        n_new = Node(value)
        if self.__head is None:
            n_new.next_node = None
            self.__head = n_new
        elif self.__head.data > value:
            n_new.next_node = self.__head
            self.__head = n_new
        else:
            tmps = self.__head
            while (tmps.next_node is not None and
                    tmps.next_node.data < value):
                tmps = tmps.next_node
            n_new.next_node = tmps.next_node
            tmps.next_node = n_new
