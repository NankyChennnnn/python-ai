# Author: bibberzz
# Created: 2026/6/2 11:11
# Project: day7
# File: task4.py
# Description: 深度优先遍历

def dfs(graph, node, visited=None):
    # 只有首个节点才会走，如果是首节点，创建一个set
    if visited is None:
        visited = set()

    # 如果被访问过直接返回
    if node is visited:
        return

    # 打印当前访问的节点
    print(f'Current visit node: {node}')

    # 把访问过的节点存入set
    visited.add(node)

    # 打印当前访问过的节点
    print(f'Visited nodes: {visited}\n')

    # 依次递归访问邻居节点
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


if __name__ == '__main__':
    # Create graph
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": []
    }

    dfs(graph, "A")
