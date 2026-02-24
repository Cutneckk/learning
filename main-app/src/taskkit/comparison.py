from context_manager import Timing
from hash_map import HashMap
from collections import deque
import random


class BenchmarkListVsDeque:
    def __init__(self, n=100000):
        self.n = n
        self.deque = deque()
        self.lst = []
        self.result = {}

    def list_append_right(self):
        with Timing("list append right") as timer:
            for i in range(self.n):
                self.lst.append(i)
        self.result['list_append_right'] = timer.elapsed_time

    def list_append_left(self):
        with Timing("list append left") as timer:
            for i in range(self.n // 10):
                self.lst.insert(0, i)
        self.result['list_append_left'] = timer.elapsed_time

    def deque_append_right(self):
        with Timing("deque append right") as timer:
            for i in range(self.n):
                self.deque.append(i)
        self.result['deque_append_right'] = timer.elapsed_time

    def deque_append_left(self):
        with Timing("deque append left") as timer:
            for i in range(self.n // 10):
                self.deque.insert(0, i)
        self.result['deque_append_left'] = timer.elapsed_time


class BenchmarkDictVsHashMap:
    def __init__(self, n=100000):
        self.n = n
        self.dct = {}
        self.hashmap = HashMap()
        self.result = {}

    def dict_insert(self, key, value):
        with Timing("dict insert") as timer:
            for k, v in zip(key, value):
                self.dct[k] = v
        self.result['dict_insert'] = timer.elapsed_time

    def dict_search(self, search_key):
        with Timing("dict search") as timer:
            for k in search_key:
                _ = self.dct.get(k)
        self.result['dict_search'] = timer.elapsed_time

    def hashmap_insert(self, key, value):
        with Timing("hashmap insert") as timer:
            for k, v in zip(key, value):
                self.hashmap.set(k, v)
        self.result['hashmap_insert'] = timer.elapsed_time

    def hashmap_search(self, search_key):
        with Timing("hashmap search") as timer:
            for k in search_key:
                _ = self.hashmap.get(k)
        self.result['hashmap_search'] = timer.elapsed_time


keys = [random.randint(1, 1000) for _ in range(10)]
values = [random.randint(1, 1000) for _ in range(10)]
search_keys = random.sample(keys, min(10000, 10))

b1 = BenchmarkListVsDeque()
b1.list_append_right()
b1.list_append_left()
b1.deque_append_right()
b1.deque_append_left()

b2 = BenchmarkDictVsHashMap()
b2.dict_insert(keys, values)
b2.hashmap_insert(keys, values)
b2.dict_search(search_keys)
b2.hashmap_search(search_keys)

print(b1.result)
print(b2.result)