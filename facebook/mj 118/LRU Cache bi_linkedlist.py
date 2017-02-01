class dList(object):
    def __init__(self):
        self.head=dListNode()
        self.tail=self.head
        self.leng=0
    def move_tolast(self,node):
        if node!=self.tail:
            # make sure node is not last
            node.last.next=node.next
            node.next.last=node.last
            node.last=self.tail
            node.next=None
            self.tail.next=node
            self.tail=node

    def remove_first(self):
        if self.head.next!=self.tail:
            head=self.head.next
            self.head.next=head.next
            head.next.last=self.head
            del head
        else:
            # !!!
            next=self.head.next
            self.head.next=None
            self.tail = self.head
            del next

    def insert_last(self,val):
        self.tail.next=dListNode(val)
        self.tail.next.last=self.tail
        self.tail=self.tail.next

class dListNode(object):
    def __init__(self,val=0):
        self.last=None
        self.next=None
        self.val=val




class LRUCache(object):
    def __init__(self,capacity):
        self.cache=dList()
        self.position={}
        self.capacity=capacity
    def put(self,key,value):
        if key in self.position:
            self.cache.move_tolast(self.position[key])
            self.position[key]=self.cache.tail

        else:
            if self.capacity==0:
                self.cache.remove_first()

            else:
                self.capacity -= 1
            self.cache.insert_last(value)
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
c.get(2)
c.put(3,2)
c.get(2)
c.get(3)
'''
c.put(3,3)
c.get(2)
c.put(4,4)
c.get(1)
c.get(3)
c.get(4)
'''
print 'lol'





