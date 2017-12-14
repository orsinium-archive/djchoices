try:
    from enum import Enum
except ImportError:
    raise ImportError("You're use Python <= 3.4. Please, install enum34: pip install enum34")


class Choices(Enum):
    def __init__(self, db, verbose):
        self.db = db
        self.verbose = verbose

    @classmethod
    def choices(cls):
        choices = cls.__members__.values()
        return tuple([(v.db, v.verbose) for v in choices])
