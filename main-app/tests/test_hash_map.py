import pytest
from taskkit.hash_map import HashMap

class TestHashMap:

    @pytest.fixture
    def hashmap(self):
        return HashMap()

    def test_set_item(self, hashmap):
        res = hashmap.set("a", 1)
        assert res == ("a", 1)
        assert hashmap.size == 1
        assert hashmap.get("a") == 1

    def test_set_duplicate(self, hashmap):
        hashmap.set("a", 1)
        hashmap.set("a", 10)
        assert hashmap.size == 1
        assert hashmap.get("a") == 10

    def test_get_item(self, hashmap):
        hashmap.set("a", 1)
        assert hashmap.get("a") == 1
        assert hashmap.get("b") is None

    def test_lru_overflow(self, hashmap):
        for i in range(100):
            hashmap.set(i, i)
            hashmap.set(99, 99)

        assert hashmap.get(98) == 98
        assert hashmap.get(99) == 99

    def test_hash_collision(self, hashmap):
        hashmap.set("a", 111)
        hashmap.set("b", 222)
        hashmap.set("c", 333)

        assert hashmap.get("a") == 111
        assert hashmap.get("b") == 222
        assert hashmap.get("c") == 333

