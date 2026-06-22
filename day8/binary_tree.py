# Author: bibberzz
# Created: 2026/6/3 08:51
# Project: day8
# File: binary_tree.py
# Description: 二叉树练习

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

    def build_tree(self, new_node: TreeNode):
        self.queue.append(new_node)  # 新节点入队
        if self.root is None:  # 没有根节点则新节点作为根节点
            self.root = new_node
        else:  # 已有根节点
            if self.queue[0].left is None:  # 根节点没左孩子
                self.queue[0].left = new_node  # 新节点作为左孩子
            else:  # 根节点有左孩子，没有右孩子
                self.queue[0].right = new_node  # 新节点作为右孩子
                self.queue.popleft()  # 出队

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

    def level_order(self):
        queue = []
        queue.append(self.root)  # 根节点先入队
        while queue:
            # 每次只pop第一个元素并打印
            node: TreeNode = queue.pop(0)
            print(node.value, end=' ')

            # 有孩子就按左右顺序入队
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        node = TreeNode(i)  # 新建一个节点
        tree.build_tree(node)  # 插入二叉树

    tree.pre_order(tree.root)  # 前序遍历 根左右
    print()
    tree.mid_order(tree.root)  # 中序遍历 左根右
    print()
    tree.last_order(tree.root)  # 后序遍历 左右根
    print()
    tree.level_order()  # 层序遍历
