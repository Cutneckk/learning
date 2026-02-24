import pytest
from taskkit.priority_queue import PriorityQueue

class TestPriorityQueue():

    @pytest.fixture
    def pq(self):
        return PriorityQueue()

    def test_priority_queue(self, pq):
        pq.add_task(1, "high")
        pq.add_task(1, "high2")
        pq.add_task(1, "high3")

        # показывает тот же порядок при равных приоритетах
        assert pq.get_task() == "high"
        assert pq.get_task() == "high2"
        assert pq.get_task() == "high3"