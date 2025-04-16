from datetime import datetime

class HashEntry:
    def __init__(self, key, value):
        self.key = key  # timestamp
        self.value = value  # distance

class HashTable:
    def __init__(self, size = 20):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                return

        self.table[index] = HashEntry(key, value)

    def getHashTable(self):
        return [(entry.key, entry.value) for entry in self.table if entry is not None]