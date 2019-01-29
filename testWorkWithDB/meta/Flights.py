

from peewee import *

from meta.DataBase import DB


class Flights(Model):
    flight_id = IntegerField(primary_key=True)
    flight_no = CharField()
    scheduled_departure = DateField()
    scheduled_arrival = DateField()
    departure_airport = CharField()
    arrival_airport = CharField()
    status = CharField()
    aircraft_code = CharField()
    actual_departure = TimestampField()
    actual_arrival = TimestampField()

    class Meta:
        database = DB().get_db()