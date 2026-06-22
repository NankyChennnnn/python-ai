# Author: bibberzz
# Created: 2026/6/3 13:32
# Project: day8
# File: task3.py
# Description: 完成二叉树层次建树，前序，中序，后序遍历

import random
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.queue = deque()

    def build_tree(self, node: TreeNode):
        if self.root is None:
            self.root = node
        else:
            if self.queue[0].left is None:
                self.queue[0].left = node
            else:
                self.queue[0].right = node
                self.queue.popleft()
        self.queue.append(node)

    def pre_order(self, node: TreeNode):
        if node:
            print(node.value, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def mid_order(self, node: TreeNode):
        if node:
            self.mid_order(node.left)
            print(node.value, end=' ')
            self.mid_order(node.right)

    def last_order(self, node: TreeNode):
        if node:
            self.last_order(node.left)
            self.last_order(node.right)
            print(node.value, end=' ')


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        new_node = TreeNode(random.randint(0, 99))
        tree.build_tree(new_node)

    tree.pre_order(tree.root)
    print()
    tree.mid_order(tree.root)
    print()
    tree.last_order(tree.root)
