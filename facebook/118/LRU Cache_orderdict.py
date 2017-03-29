from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value=self.cache.pop(key)
            self.cache[key]=value
            return value
        except KeyError:
            return -1



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void

        """
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key]=value


dic=OrderedDict()
dic[0]=1
dic[1]=2
dic[3]=5
print
del dic[len(dic)-1]
for i in dic:
    print i