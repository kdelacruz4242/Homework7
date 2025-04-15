class HashInit:

    def __init__(self, key, value):
        self.key = value
        self.value = value

class HashTable:

    def __init__(self, size = 20):
        self.size = size
        self.value = value

   def _hash(self, key):
        return hash(key) % self.size

