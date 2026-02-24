import heapq
from collections import deque


class PriorityQueue:

    def __init__(self):
        self._priority_map = {}
        self._min_heap = []
        self._total_tasks = 0

    def add_task(self, priority: int, name: str):

        if priority not in self._priority_map:
            self._priority_map[priority] = deque()
            heapq.heappush(self._min_heap, priority)

        self._priority_map[priority].append(name)
        self._total_tasks += 1
        return f"added: {name} (priority: {priority})"

    def get_task(self):

        if self.is_empty():
            raise IndexError("empty queue")

        min_priority = self._min_heap[0]
        task = self._priority_map[min_priority].popleft()
        self._total_tasks -= 1

        if not self._priority_map[min_priority]:
            del self._priority_map[min_priority]
            heapq.heappop(self._min_heap)

        return task

    def is_empty(self):
        return self._total_tasks == 0

    def struct(self):
        return [(priority ,[x for x in name]) for priority, name in self._priority_map.items()]


pq = PriorityQueue()

pq.add_task(3, "low")
pq.add_task(1, "high")
pq.add_task(1, "high")
pq.add_task(2, "medium")
pq.add_task(1, "high")

print(pq.struct())

while not pq.is_empty():
    print(pq.get_task())


