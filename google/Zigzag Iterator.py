# -*- coding: utf-8 -*-
'''
init的时候，有2个tuple，每个tuple都是(list长度，遍历器),next的时候pop出来
一个，如果长度>1就append进去到最后，而且长度-1
'''
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return iter.next()

    def hasNext(self):
        return bool(self.data)

v1 = [1, 2]
v2 = [3, 4, 5, 6]
i,v=ZigzagIterator(v1,v2),[]
while i.hasNext():
    v.append(i.next())