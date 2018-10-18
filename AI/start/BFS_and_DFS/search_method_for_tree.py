#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from data_struct import Stack,Queue,TreeNode


class Tree(object):
    def __init__(self,rootNode = None):
        self.rootNode = rootNode

    def insert_node(self,father_node,inserted_node):
        node = self.dfs_search(father_node)

        if node is None:
            return False
        else:
            node.sub_nodes.append(inserted_node)
            return True

    def delete_node(self,value):
        if self.rootNode is None:
            return False
        else:
            if self.rootNode.value == value:
                self.rootNode = None
                return True
            else:
                stack = Stack()
                stack.push(self.rootNode)

                while stack.top() is not None:
                    node = stack.pop()
                    print(node.value)
                    for sub_node in node.sub_nodes:
                        if sub_node.value == value:
                            sub_node = None
                            node.sub_nodes.delete(sub_node)
                            return True
                        stack.push(sub_node)
            return False

    def set_node_value(self,origin_value,new_value):
        node = self.dfs_search(origin_value)
        if node is None:
            return False
        else:
            node.set_value(new_value)
            return True
    
    def dfs_search(self,value):
        if self.rootNode is None:
            return None
        elif len(self.rootNode.sub_nodes) is 0:
            if value == self.rootNode.value:
                return self.rootNode
            else:
                return None
        else:
            stack = Stack()
            stack.push(self.rootNode)

            while stack.top() is not None:
                node = stack.pop()
#                print(node.value)
                if node.value == value:
                    return node
                else:
                    for sub_node in node.sub_nodes:
                        stack.push(sub_node)
            return None

    def bfs_search(self,value):
        if self.rootNode == None:
            return None
        elif len(self.rootNode.sub_nodes) is 0:
            if value == self.rootNode.value:
                return self.rootNode
            else:
                return None
        else:
            queue = Queue()
            queue.enQueue(self.rootNode)

            while queue.front() is not None:
                node = queue.deQueue()
#                print(node.value)

                if node.value == value:
                    return node
                else:
                    for sub_node in node.sub_nodes:
                        queue.enQueue(sub_node)
            return None

    def dfs_search_shortest_path(self,value):
        node = self.dfs_search(value)
        if node is not None:
            path = []
            path.append(node)
            while node.father_node is not None:
                node = node.father_node
                path.append(node)
            return reversed(path)
        else:
            return None

    def bfs_search_shortest_path(self,value):
        node = self.bfs_search(value)
        if node is not None:
            path = []
            path.append(node)
            while node.father_node is not None:
                node = node.father_node
                path.append(node)
            return reversed(path)
        else:
            return None


# for test
if __name__ == "__main__":
    treeNode25 = TreeNode(25,None)

    treeNode36 = TreeNode(36,treeNode25)
    treeNode55 = TreeNode(55,treeNode25)
    treeNode129 = TreeNode(129,treeNode25)

    treeNode12 = TreeNode(12,treeNode36)
    treeNode21 = TreeNode(21,treeNode36)

    treeNode33 = TreeNode(33,treeNode55)
    treeNode52 = TreeNode(52,treeNode55)

    treeNode100 = TreeNode(100,treeNode129)
    treeNode110 = TreeNode(110,treeNode129)

    treeNode9 = TreeNode(9,treeNode12)
    treeNode8 = TreeNode(8,treeNode12)

    treeNode32 = TreeNode(32,treeNode33)
    treeNode31 = TreeNode(31,treeNode33)

    treeNode4 = TreeNode(4,treeNode9)

    print("print TreeNode:")
    print(treeNode25)

    tree = Tree(treeNode25)

    # 取消 Tree 中 dfs_search 的 print 注释观看结果
    # print("\n*************")
    # print("DFS_search:")
    # tree.dfs_search(31)

    print("\n***** *****")
    for node in tree.dfs_search_shortest_path(31):
        print(node.value)

    # 取消 Tree 中 bfs_search 的 print 注释观看结果
    # print("\n*************")
    # print("BFS_search:")
    # tree.bfs_search(31)

    print("\n***** *****")
    for node in tree.bfs_search_shortest_path(31):
        print(node.value)