# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510
# Date: 2018/9/22
# version: 1.0
# python_version: 3.62

from data_struct import Stack,Queue,BinarySearchTreeNode as BSTN

class BinarySearchTree(object):
    def __init__(self,rootNode):
        self.rootNode = rootNode

    def is_empty(self):
        return False if (self.rootNode is None) else True

    def make_empty(self):
        self.rootNode = None

    def set_new_root(self,new_root_node):
        self.rootNode = new_root_node

    def find(self,searched_value):
        node = self.rootNode
        while node is not None:
            if searched_value is node.value:
                return node
            elif searched_value < node.value:
                node = node.sub_nodes[0]
            else:
                node = node.sub_nodes[1]
        return None

    def findMin(self):
        node = self.rootNode
        while node is not None:
            if node.sub_nodes[0] is None:
                return node
            else:
                node = node.sub_nodes[0]
        return node

    def findMax(self):
        node = self.rootNode
        while node is not None:
            if node.sub_nodes[1] is None:
                return node
            node = node.sub_nodes[1]
        return node

    def preIndexRead(self):
        stack = Stack()
        node = self.rootNode

        while not ((node is None) and (stack.top() is None)):
            while node is not None:
                print(node.value)
                stack.push(node)
                node = node.sub_nodes[0]
            node = stack.pop().sub_nodes[1]

    def midIndexRead(self):
        stack = Stack()
        node = self.rootNode

        while not ((node is None) and (stack.top() is None)):
            while node is not None:
                stack.push(node)
                node = node.sub_nodes[0]

            node = stack.pop()
            print(node.value)
            node = node.sub_nodes[1]

    def postIndexRead(self):
        stack = Stack()
        node = self.rootNode
        lastVisited = node

        while node is not None or not stack.isEmpty():
            while node is not None:
                stack.push(node)
                node = node.sub_nodes[0]

            node = stack.top()

            if node.sub_nodes[1] is None or node.sub_nodes[1] is lastVisited:
                print(node.value)
                lastVisited = stack.pop()
                node = None
            else:
                node = node.sub_nodes[1]

    def levelRead(self):
        queue = Queue()
        queue.enQueue(self.rootNode)

        level_list = [queue.front()]
        next_level_list = []
        level = 1
        print("level:", level)

        while queue.front() is not None:
            if len(level_list) is 0:
                temp = next_level_list
                next_level_list = level_list
                level_list = temp

                level += 1
                print("\nlevel:",level)

            front = queue.deQueue()
            print(front.value,end="\t")
            level_list.remove(front)

            for sub_node in front.sub_nodes:
                if sub_node is not None:
                    queue.enQueue(sub_node)
                    next_level_list.append(sub_node)

    def insert_node(self,inserted_node):
        node = self.rootNode
        try:
            while node is not None:
                if inserted_node.value is node.value:
                    return False
                elif (inserted_node.value < node.value):
                    if (node.sub_nodes[0] is None):
                        node.sub_nodes[0] = inserted_node
                    else:
                        node = node.sub_nodes[0]
                elif (inserted_node.value > node.value):
                    if (node.sub_nodes[1] is None):
                        node.sub_nodes[1] = inserted_node
                    else:
                        node = node.sub_nodes[1]
            return True
        except:
            return False

    def delete_node(self,deleted_value):
        node = self.rootNode
        while node is not None:
            if deleted_value is node.value:
                node = None
                return True
            elif deleted_value < node.value:
                node = node.sub_nodes[0]
            else:
                node = node.sub_nodes[1]
        return False

if __name__  == "__main__":
    node50 = BSTN(50, None)

    node20 = BSTN(20, node50)
    node80 = BSTN(80, node50)

    node10 = BSTN(10, node20)
    node32 = BSTN(32, node20)
    node65 = BSTN(65, node80)
    node100 = BSTN(100, node80)

    node15 = BSTN(15, node10)
    node25 = BSTN(25, node32)
    node40 = BSTN(40, node32)
    node92 = BSTN(92, node100)
    node112 = BSTN(112, node100)

    node13 = BSTN(13, node15)
    node16 = BSTN(16, node15)
    node37 = BSTN(37, node40)
    node201 = BSTN(201, node112)

    bst = BinarySearchTree(node50)

    bst.levelRead()
    # print(bst.findMin())
    # print(bst.findMax
    # bst.levelRead()
    # bst.preIndexRead()
    # bst.midIndexRead()
    # bst.postIndexRead()

