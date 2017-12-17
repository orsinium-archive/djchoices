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

    @classmethod
    def by_db(cls, db):
        members = {member.db: member for member in cls.__members__.values()}
        return members[db]

    @classmethod
    def by_verbose(cls, verbose):
        members = {member.verbose: member for member in cls.__members__.values()}
        return members[verbose]

    @classmethod
    def verbose_by_db(cls, db):
        return cls.by_db(db).verbose

    @classmethod
    def db_by_verbose(cls, verbose):
        return cls.by_verbose(verbose).db
