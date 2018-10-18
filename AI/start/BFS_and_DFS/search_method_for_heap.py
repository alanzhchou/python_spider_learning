#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510 
# Date: 2018/9/23
# version: 1.0
# python_version: 3.62
from data_struct import HeapNode

class MaxHeap(object):
    def __init__(self,root_node):
        self.root_node = root_node

    def is_empty(self):
        return True if self.root_node is None else False

    def make_empty(self):
        try:
            self.root_node = None
        except:
            print("置空失败")

    def insert(self,inserted_value):
        inserted_node = HeapNode(inserted_value)

        if self.root_node is None:
            self.root_node = HeapNode(inserted_value)
            return True
        else:
            node = self.root_node
            while node is not None:
                if inserted_value == node.value:
                    return False
                if inserted_value < node.value:
                    if node.next is None:
                        node.next = inserted_node
                        inserted_node.pre = node
                        return True
                    else:
                        node = node.next
                        continue
                else: # inserted_value > node.value:
                    if node.pre is None:
                        node.pre = inserted_node
                        inserted_node.next = node
                        self.root_node = inserted_node
                    else:
                        temp = node
                        temp.pre.next = inserted_node
                        inserted_node.pre = temp.pre
                        inserted_node.next = temp
                        temp.pre = inserted_node
                    return True
            return False

    def insert_list(self,list):
        try:
            for ele in list:
                self.insert(ele)
            return True
        except:
            return False

    def detele(self,value):
        node = self.root_node

        while node is not None:
            if node.value != value:
                node = node.next
                continue
            else:
                if node.pre is None:
                    if node.next is not None:
                        self.root_node = node.next
                        self.root_node.pre = None
                    else:
                        self.root_node = None
                else:
                    if node.next is not None:
                        node.pre.next = node.next
                        node.next.pre = node.pre
                        node = None
                    else:
                        node.pre.next = None
                return True
        return False

    def deQueue(self):
        return self.detele(self.root_node.value)

    def find(self,value):
        node = self.root_node

        while node is not None:
            if node.value != value:
                node = node.next
                continue
            else:
                return node

        return None

    def __str__(self):
        info = ""
        node = self.root_node

        i = 1
        while node is not None:
            info += repr(node.value) + "\t"
            if i%2 == 1:
                info += "\n"
            i += 1

            node = node.next
        return info

# to do
class MinHeap(object):
    def __init__(self):
        pass

if __name__ == "__main__":
    node = HeapNode(55)
    print(node)

    maxHeap = MaxHeap(node)
    maxHeap.insert_list([20,50,100,150])
    print(maxHeap)

    maxHeap.detele(100)
    print(maxHeap)

    print(maxHeap.find(50))
    print(maxHeap.find(20))

    maxHeap.deQueue()
    print(maxHeap)

