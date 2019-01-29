from meta.DataBase import DB
from peewee import *


class Bookings(Model):

    book_ref = CharField(primary_key=True)
    book_date = DateField()
    total_amount = FloatField()

    class Meta:
        database = DB().get_db()