from peewee import *
from meta.DataBase import DB
from meta.Flights import Flights
from meta.Tickets import Tickets


class Ticket_Flights(Model):
    ticket_no = ForeignKeyField(Tickets, db_column='ticket_no')
    flight_id = ForeignKeyField(Flights, db_column='flight_id')
    fare_conditions = CharField()
    amount = IntegerField()
    class Meta:
        database = DB().get_db()