# -*- coding: utf-8 -*-
'''
用 一个double linked list 存cache，hashtable存<key，node>
node: key,val,next,last
'''
import gc

class dList(object):
    def __init__(self):
        self.head=None
        self.tail=self.head
        self.leng=0
    def move_tolast(self,node):
        if node!=self.tail:
            # make sure node is not last
            if node.last!=None:
                node.last.next=node.next
            node.next.last=node.last
            node.last=self.tail
            node.next=None
            self.tail.next=node
            self.tail=node

    def remove_first(self):
        first_key=self.head.key
        if self.head!=self.tail:
            head=self.head
            self.head=self.head.next
            if self.head!=None:
                self.head.last=None

        else:
            self.head=None
            self.tail=self.head
        return first_key

    def insert_last(self,key,val):
        if self.head==None:
            self.head=dListNode(key,val)
            self.tail=self.head
        else:
            self.tail.next=dListNode(key,val)
            self.tail.next.last=self.tail
            self.tail=self.tail.next

class dListNode(object):
    def __init__(self,key=0,val=0):
        self.last=None
        self.next=None
        self.key=key
        self.val=val





class LRUCache(object):
    def __init__(self,capacity):
        self.cache=dList()
        self.position={}
        self.capacity=capacity
    def put(self,key,value):
        if key in self.position and self.position[key]!=None:
            self.cache.move_tolast(self.position[key])
            self.position[key]=self.cache.tail

        else:
            if self.capacity==0:
                first_key=self.cache.remove_first()
                self.position[first_key]=None
            else:
                self.capacity -= 1
            self.cache.insert_last(key,value)
            self.position[key]=self.cache.tail
    def get(self,key):
        if key in self.position and self.position[key]!=None:
            self.cache.move_tolast(self.position[key])
            self.position[key]=self.cache.tail
            return self.cache.tail.val
        else:
            return -1
c=LRUCache(1)
c.put(2,1)
print c.get(2)
c.put(3,2)
print c.get(2)
print c.get(3)
c.put(2,1)
print c.get(2)
print c.get(3)
'''
c.put(3,3)
c.get(2)
c.put(4,4)
c.get(1)
c.get(3)
c.get(4)
'''
print 'lol'





