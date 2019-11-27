from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.dict = OrderedDict()

    def get(self, key):
        if key not in self.dict:
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value

    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        self.dict[key] = value
        if len(self.dict) > self.cap:
            self.dict.popitem(last = False)
