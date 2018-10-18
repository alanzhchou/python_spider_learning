# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510
# Date: 2018/9/22
# version: 1.0
# python_version: 3.62

from collections import *

class Stack(object):
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def makeEmpty(self):
        try:
            self.elements.clear()
            return True
        except:
            return False

    def push(self,element):
        try:
            self.elements.append(element)
            return True
        except:
            print("置入失败")
            return False

    def top(self):
        if len(self.elements) != 0:
            return self.elements[len(self.elements) - 1]
        else:
            return None

    def pop(self):
        try:
            return self.elements.pop()
        except:
            print("弹出错误")

    def __str__(self):
        stack_info = "***** ****** ***** *****\n"
        for element in reversed(self.elements):
            stack_info += str(element) + "\n"

        stack_info += "***** ****** ***** *****\n"
        return stack_info

# 最后一个为head 第一个为tail
class Queue(object):
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def makeEmpty(self):
        try:
            self.elements.clear()
            return True
        except:
            return False

    def front(self):
        if len(self.elements) != 0:
            return self.elements[len(self.elements)-1]
        else:
            return None

    def enQueue(self,element):
        try:
            if len(self.elements) == 0:
                self.elements.append(element)
            else:
                self.elements.insert(0, element)
        except:
            print("入队列失败")

    def deQueue(self):
        return self.elements.pop()

class TreeNode(object):
    def __init__(self, x, father_node):
        self.value = x
        self.father_node = father_node
        self.sub_nodes = []
        if self.father_node is not None:
            self.father_node.sub_nodes.append(self)

    def __str__(self):
        '''
        father: X
        A:
        {
            B
            C
        }
        '''
        info = ""
        if self.father_node is not None:
            info += "father: " + repr(self.father_node.value) + "\n"
        else:
            info += "father: " + repr(None) + "\n"

        info += repr(self.value) + ":\n{\n"
        for sub_node in self.sub_nodes:
            info += "\t" + repr(sub_node.value) + "\n"
        info += "}"

        return info

    def set_value(self, new_value):
        self.value = new_value

    def add_sub_node(self, sub_node):
        try:
            self.sub_nodes.append(sub_node)
            sub_node.father_node = self
        except:
            print("增加字节点错误")

class GraphNode(object):
    def __init__(self, name="", route=None):
        self.name = name
        self.route = route

    def __str__(self):
        """
        A:
        {
            B: 15
            C: 20
        }
        """
        info = self.name + ":\n{\n"
        for node in self.route.keys():
            info += "\t" + node + ": " + repr(self.route[node]) + "\n"

        info += "}"
        return info

    def set_name(self, new_name):
        self.name = new_name

class BinarySearchTreeNode(object):
    def __init__(self,value,father_node,left=None,right=None):
        self.value = value
        self.father_node = father_node
        self.sub_nodes = [None,None]

        if self.father_node is not None:
            if (self.value < father_node.value) and (father_node.sub_nodes[0] is None):
                self.father_node.sub_nodes[0] = self
            elif (self.value > father_node.value) and (father_node.sub_nodes[1] is None):
                self.father_node.sub_nodes[1] = self

        if left is None or left < self.value:
            self.sub_nodes[0] = left
        if right is None or right > self.value:
            self.sub_nodes[1] = right

    def set_value(self,new_value):
        self.value = new_value

    def add_sub_node(self,added_node):
        try:
            if (added_node.value < self.value) and self.sub_nodes[0] is None:
                self.sub_nodes[0] = added_node
                added_node.father_node = self
            elif (added_node.value > self.value) and self.sub_nodes[1] is None:
                self.sub_nodes[1] = added_node
                added_node.father_node = self
        except:
            print("添加子节点错误")

    def __str__(self):
        '''
        father: X
        A:
        {
            left: B
            right: C
        }
        '''
        info = ""
        if self.father_node is not None:
            info += "father: " + repr(self.father_node.value) + "\n"
        else:
            info += "father: " + repr(None) + "\n"

        info += repr(self.value) + ":\n{\n"

        if self.sub_nodes[0] is not None:
            info += "\tleft: " + repr(self.sub_nodes[0].value) + "\n"
        else:
            info += "\tleft: " + repr("None") + "\n"

        if self.sub_nodes[1] is not None:
            info += "\tright: " + repr(self.sub_nodes[1].value) + "\n"
        else:
            info += "\tright: " + repr("None") + "\n"

        info += "}"
        return info

class HeapNode(object):
    def __init__(self,value):
        self.value = value
        self.pre = None
        self.next = None

    def __str__(self):
        info = "{\n" + "\tvalue: " + repr(self.value) + "\n\n"
        if self.pre is not None:
            info += "\tpre: " + repr(self.pre.value) + "\n"
        else:
            info += "\tpre: None" + "\n"
        if self.next is not None:
            info += "\tnext: " + repr(self.next.value) + "\n"
        else:
            info += "\tnext: None" + "\n"
        return info + "}"

# max
class MaxPriorityQueue(object):
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def make_empty(self):
        try:
            self.elements.clear()
            return True
        except:
            return False

    def front(self):
        if len(self.elements) != 0:
            return self.elements[0]
        else:
            return None

    def en_queue_with_priority(self,inserted_priority_value,node):
        try:
            if len(self.elements) == 0:
                self.elements.insert(0, [inserted_priority_value, node])
                return True
            else:
                i = 0
                for ele in self.elements:
                    priority = ele[0]
                    if priority < inserted_priority_value:
                        self.elements.insert(i, [inserted_priority_value, node])
                        return True
                    if priority == inserted_priority_value:
                        return False
                    i += 1
                self.elements.append([inserted_priority_value, node])
                return True
        except:
            return False
            print("入队列失败")

    def deQueue(self):
        if len(self.elements) is not 0:
            info = self.elements[0]
            del self.elements[0]
            return info[1]
        return None

    def __str__(self):
        info = ""

        i = 1
        for ele in self.elements:
            info += repr(ele) + "\t"
            if i%2 == 1:
                info += "\n"
            i += 1
        return info

# min
class MinPriorityQueue(object):
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def makeEmpty(self):
        try:
            self.elements.clear()
            return True
        except:
            return False

    def front(self):
        if len(self.elements) != 0:
            return self.elements[len(self.elements) - 1]
        else:
            return None

    def en_queue_with_priority(self,inserted_priority_value,node):
        try:
            if len(self.elements) == 0:
                self.elements.insert(0, [inserted_priority_value, node])
                return True
            else:
                i = 0
                for ele in self.elements:
                    priority = ele[0]
                    if priority < inserted_priority_value:
                        self.elements.insert(i, [inserted_priority_value, node])
                        return True
                    if priority == inserted_priority_value:
                        return False
                    i += 1
                self.elements.append([inserted_priority_value, node])
                return True
        except:
            return False
            print("入队列失败")

    def deQueue(self):
        if len(self.elements) is not 0:
            return self.elements.pop()[1]
        return None

    def __str__(self):
        info = ""

        i = 1
        for ele in self.elements:
            info += repr(ele) + "\t"
            if i%2 == 1:
                info += "\n"
            i += 1
        return info


if __name__ == "__main__":
    # queue = MaxPriorityQueue()
    # queue.en_queue_with_priority(5,"a")
    # queue.en_queue_with_priority(51,"b")
    # queue.en_queue_with_priority(500,"c")
    # print(queue)
    # queue.deQueue()
    # print(queue)

    queue2 = MinPriorityQueue()
    queue2.en_queue_with_priority(329,"a")
    queue2.en_queue_with_priority(253,"b")
    queue2.en_queue_with_priority(374,"c")
    print(queue2)
    queue2.deQueue()
    print(queue2)