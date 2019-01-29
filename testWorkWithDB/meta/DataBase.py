from peewee import *

class DB:
    db = PostgresqlDatabase('demo')
    con = None

    def __init__(self):
        self.db = PostgresqlDatabase('demo')

    def get_db(self):
        return self.db

    def close_con(self):
        self.db.close()
