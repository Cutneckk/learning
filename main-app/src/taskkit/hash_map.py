from .lru import lru

class HashMap:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _probe(self, key, i):
        return (self._hash(key) + i * i) % self.capacity

    @lru(maxsize=50)
    def set(self, key, value):
        if self.size == self.capacity:
            raise Exception("full")

        for i in range(self.capacity):
            idx = self._probe(key, i)

            if self.keys[idx] is None or self.keys[idx] == key:
                if self.keys[idx] is None:
                    self.size += 1
                self.keys[idx] = key
                self.values[idx] = value
                return key, value

        raise Exception("insert failed")

    def get(self, key):
        for i in range(self.capacity):
            idx = self._probe(key, i)

            if self.keys[idx] == key:
                return self.values[idx]

            if self.keys[idx] is None:
                break

        return None


h = HashMap()
h.set("a", 1)
h.set("b", 2)
h.set("b", 2)
print(h.get("a"))
print(h.get("b"))



