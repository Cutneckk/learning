import bisect
from array import array
from datetime import datetime, timedelta


class TaskScheduler:
    def __init__(self):
        self.deadlines = []
        self.task_ids = array('I')

    def add_task(self, task_id: int, deadline):
        deadline = datetime.now() + timedelta(hours=deadline)
        timestamp = int(deadline.timestamp())
        pos = bisect.bisect_left(self.deadlines, timestamp)

        self.deadlines.insert(pos, timestamp)
        self.task_ids.insert(pos, task_id)

    def get_next_task(self):

        if not self.deadlines:
            return None

        timestamp = self.deadlines.pop(0)
        task_id = self.task_ids.pop(0)

        return task_id, datetime.fromtimestamp(timestamp)


scheduler = TaskScheduler()

# указываем время в часах
scheduler.add_task(101, 2)   # +2 часа
scheduler.add_task(102, 0.5) # +30 минут
scheduler.add_task(103, 24)  # +24 часа

print(scheduler.get_next_task())
print(scheduler.get_next_task())
print(scheduler.get_next_task())
print(scheduler.get_next_task())


