import unittest
from unittest import TestCase

class TestStack(TestCase):
    def test_push_pop(self):
        x = Stack()

        x.push(1)
        x.push(2)
        x.push(3)

        with self.subTest('Test pop method'):
            for num in (3, 2, 1):
                self.assertEqual(x.pop(), num)   
        
        with self.assertRaises(StackIsEmpty):
            x.pop()


class StackIsEmpty(Exception):
    pass

class Stack():
    class Node():
        def __init__(self, x, prev=None):
            self.value = x
            self.prev = prev

    def __init__(self):
        self.node = None

    def push(self, x):
        self.node = self.Node(x, self.node)

    def pop(self):
        if self.node:
            value = self.node.value
            self.node = self.node.prev
            return value
        raise StackIsEmpty


    def print(self):
        node = self.node
        while node:
            print(node.value)
            node = node.prev

if __name__ == '__main__':
    unittest.main()
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
