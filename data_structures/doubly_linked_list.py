"""
Doubly Linked List

None <-- N1 <--> N2 <--> N3 --> None
"""


class Node:

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.val = value
        self._prev = prev
        self._next = next

    # def __init__(self, value, prev=None, next=None):
    #     self.__init__(None, value, prev, next)

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, p):
        if p == self:
            raise Exception("A node cannot point to itself!")
        self._prev = p

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        if n == self:
            raise Exception("A node cannot point to itself!")
        self._next = n


class DoublyLinkedList:

    def __init__(self):
        self._start = None
        self._end = None

    def get_start_node(self):
        return self._start

    def add_to_end(self, node: Node):
        """Add a node to the end of the list"""
        assert node is not None, "not a valid node"
        if self._start is None and self._end is None:
            # Adding first node
            self._start = node
            self._end = node
            node.next = None
            node.prev = None
            return
        node.prev = self._end
        node.next = None
        self._end.next = node
        self._end = node

    def add_to_beginning(self, node: Node):
        """Add a node to the beginning of the list"""
        assert node is not None, "not a valid node"
        if self._start is None and self._end is None:
            self._start = node
            self._end = node
            node.prev = None
            node.next = None
            return
        node.next = self._start
        node.prev = None
        self._start.prev = node
        self._start = node

    def move_to_end(self, node: Node):
        """Move a node to the end of the list"""
        assert node is not None, "not a valid node"
        if self._end == node:
            return  # Already at end
        if self._start == node:
            if node.next:
                self._start = node.next
                self._start.prev = None
        self._end.next = node
        node.prev = self._end
        self._end = node
        self._end.next = None

    def delete(self, node: Node):
        """Delete a node from the list"""
        assert node is not None, "not a valid node"
        if self._start == node:
            self._start = node.next
        if self._end == node:
            self._end = node.prev
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        del node

    def delete_from_beginning(self):
        """Delete a node from the beginning of the list"""
        if self._start is None:
            return
        if self._start == self._end:  # when only 1 item exists in list
            self._start = None
            self._end = None
            return
        self._start = self._start.next