import IList.py

#节点类描述
class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#单链表类描述
class LinkList(IList):
    def __init__(self):
        self.head = Node() #构造函数初始化头节点

    def creat(self, l, order):
        if order:
            self.creat_tail