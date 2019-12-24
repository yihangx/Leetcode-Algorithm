from random import choice
class Insert_Delete_GetRandom:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def delete(self, val):
        if val in self.dict:
            last, index = self.list[-1], self.dict[val]
            self.list[index], self.dict[last] = last, index
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self.list)
