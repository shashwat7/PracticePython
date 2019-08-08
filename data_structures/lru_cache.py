"""
Design a data structure for LRU Cache. It should support the following operations: get and set.

get(key) – Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

set(key, value) – Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

from data_structures.doubly_linked_list import DoublyLinkedList, Node


class LruCache:

    def __init__(self, capacity):
        self._cache = {} # dictionary to contain key-value
        self._doubly_linked_list = DoublyLinkedList()
        self._capacity = capacity
        self._size = 0

    def get(self, key):
        if key not in self._cache:
            return -1
        else:
            node = self._cache[key]
            self._doubly_linked_list.move_to_end(node)
            return node.val

    def set(self, key, value):
        if self._size == self._capacity:
            # Cache is full delete least recently used node
            self._cache.pop(self._doubly_linked_list.get_start_node().key)
            self._doubly_linked_list.delete_from_beginning()
            self._size = self._size - 1

        if key in self._cache:
            # Key already exists, need to delete it from doubly linked list first
            self._doubly_linked_list.delete(self._cache[key])
            self._size = self._size - 1

        node = Node(key, value)
        self._cache[key] = node
        self._doubly_linked_list.add_to_end(node)
        self._size = self._size + 1

    def print(self):
        for k in self._cache:
            print('{} = {}'.format(k, self._cache[k].val))
