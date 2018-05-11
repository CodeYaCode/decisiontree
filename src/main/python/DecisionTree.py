# -*- coding: utf-8 -*-
# Decision tree
class DecisionTree:
    def __init__(self, value):
        self.root = Node(value)
        pass

    def show(self, node):
        node.show()
        if node.left is not None:
            node.left.show()
        if node.right is not None:
            node.right.show()


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def show(self):
        print(self.value)