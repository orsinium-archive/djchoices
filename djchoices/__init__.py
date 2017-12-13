try:
    from enum import Enum
except ImportError:
    raise ImportError("You're use Python <= 3.4. Please, install enum34: pip install enum34")
import inspect


class Choices(Enum):
    def __init__(self, db, verbose):
        self.db = db
        self.verbose = verbose

    @classmethod
    def choices(cls):
        members = inspect.getmembers(cls, lambda m: not(inspect.isroutine(m)))
        props = [m for m in members if not(m[0][:2] == '__')]
        choices = tuple([(v.db, v.verbose) for k, v in props])
        return choices
