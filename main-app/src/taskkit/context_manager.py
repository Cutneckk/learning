import time
import logging


class Timing:

    def __init__(self, name="Operation"):
        self.name = name
        self.start_time = None
        self.elapsed_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.perf_counter() - self.start_time
        return False


class suppress:
    def __init__(self, *exc_types):
        self.exc_types = exc_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exc_types):
            logging.debug(f"suppressed exception: {exc_type.__name__}: {exc_val}")
            return True
        return False
