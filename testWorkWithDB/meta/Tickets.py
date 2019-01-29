from meta.DataBase import DB
from meta.Bookings import Bookings
from peewee import *



class Tickets(Model):
    base = None
    ticket_no = CharField(primary_key=True)
    book_ref = ForeignKeyField(Bookings, db_column='book_ref')
    passenger_id = CharField()
    passenger_name = TextField()
    contact_data = CharField()


    class Meta:
        database = DB().get_db()

    def get_all_from_base(self):
        return Tickets.select()



