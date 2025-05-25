import sqlite3

class Database:
    _connection = None
    _cursor = None
    _db_file = 'orm_data.db'

    @classmethod
    def connect(cls):
        if cls._connection is None:
            cls._connection = sqlite3.connect(cls._db_file)
            cls._cursor = cls._connection.cursor()
        return cls._connection

    @classmethod
    def execute(cls, query, params=None):
        if cls._connection is None:
            cls.connect()
        if params is None:
            params = []
        cls._cursor.execute(query, params)
        cls._connection.commit()
        return cls._cursor

    @classmethod
    def fetchone(cls):
        return cls._cursor.fetchone()

    @classmethod
    def fetchall(cls):
        return cls._cursor.fetchall()

    @classmethod
    def close(cls):
        if cls._connection:
            cls._connection.close()
            cls._connection = None
            cls._cursor = None