class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [None] * 10000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = hash(key) % 10000
        if self.array[index] != None:
            dummy = self.array[index]  # linked list of key,values
            prev = None
            while dummy != None:
                if dummy.key == key:
                    dummy.value = value
                    return
                prev = dummy
                dummy = dummy.next
            prev.next = ListNode(key, value)
        else:
            self.array[index] = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        index = hash(key) % 10000
        if self.array[index] != None:
            dummy = self.array[index]
            while dummy:
                if dummy.key == key:
                    return dummy.value
                dummy = dummy.next
        return -1

    def print_at_index(self, key):
        index = hash(key) % 10000
        dummy = self.array[index]
        while dummy:
            print(dummy.key, end="")
        print()

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = hash(key) % 10000
        dummy = self.array[index]

        if dummy != None:
            prev = dummy
            if dummy.key == key:
                dummy = dummy.next
                self.array[index] = dummy
                return

            while dummy and dummy.key != key:
                prev = dummy
                dummy = dummy.next

            if dummy == None:
                return

            prev.next = dummy.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
