class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [None] * 10000

    def add(self, key: int) -> None:
        index = hash(key) % 10000
        if self.array[index] == None:
            self.array[index] = [key]
        else:
            if key not in self.array[index]:
                self.array[index].append(key)

    def remove(self, key: int) -> None:
        index = hash(key) % 10000
        if self.array[index] != None:
            if key in self.array[index]:
                self.array[index].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = hash(key) % 10000
        if self.array[index] != None:
            if key in self.array[index]:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
