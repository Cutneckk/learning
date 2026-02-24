from collections import deque


class Task:
    def __init__(self, ids, priority, name):
        self.id = ids
        self.priority = priority
        self.name = name

    def __repr__(self):
        return f"Task({self.id}, {self.priority}, '{self.name}')"


class Pipeline:
    @staticmethod
    def filter_tasks(tasks, predicate):
        def gen():
            for task in tasks:
                if predicate(task):
                    yield task
        yield from gen()

    @staticmethod
    def map_tasks(tasks, func):
        def gen():
            for task in tasks:
                yield func(task)
        yield from gen()

    def get_priority(self, tasks, priority):
        yield from self.filter_tasks(tasks, lambda x: x.priority == priority)

    def get_names(self, tasks):
        yield from self.map_tasks(tasks, lambda x: x.name)

    def get_ids(self, tasks):
        yield from self.map_tasks(tasks, lambda x: x.id)


class SlidingWindow:
    def __init__(self, obj, k):
        self.obj = obj
        self.k = k

    def __iter__(self):
        window = deque(maxlen=self.k)

        for item in self.obj:
            window.append(item)
            if len(window) == self.k:
                yield tuple(window)


t = [
    Task(1, "high", "fix"),
    Task(2, "low", "fix"),
    Task(3, "high", "tests"),
    Task(4, "medium", "deploy"),
]

pl = Pipeline()

# фильтрация по приоритету
high_priority = pl.get_priority(t, "high")
for task in high_priority:
    print(task)

# фильтрация по id
ids = pl.get_ids(t)
for w in ids:
    print(w)

# фильтрация по названию
names = pl.get_names(t)
for w in names:
    print(w)

# фильрация по id через скользящее окно
high_priority_ids = pl.get_ids(pl.get_priority(t, "high"))
window = SlidingWindow(high_priority_ids, 2)
for w in window:
    print(w)
