import functools
from collections import deque

def lru(maxsize: int):
    def decorator(func):
        cache = {}
        order = deque()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))
            if key in cache:
                order.remove(key)
                order.append(key)
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result
            order.append(key)

            if len(order) > maxsize:
                oldest = order.popleft()
                del cache[oldest]
            return result

        return wrapper
    return decorator