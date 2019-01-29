"""
Краткое описание
все что в пакете "meta" -- модели базы, пока не полные
исключая DataBase.py.  Это класс для подключения к локальной БД
"""

from meta.Flights import Flights
from meta.TicketFlights import Ticket_Flights
from meta.Tickets import Tickets
from datetime import date, datetime
import json


class testCon:
    # Возвращает "условные" данные в формате json (пока вроде не очень правильно...)
    def get_data(self):
        query = (Flights.select(Flights.flight_id,
                                Flights.departure_airport,
                                Flights.arrival_airport,
                                Tickets.passenger_name). \
                 join(Ticket_Flights). \
                 join(Tickets). \
                 where(Flights.scheduled_departure >= datetime(2017, 8, 15),
                       Flights.scheduled_departure <= datetime(2017, 8, 28)). \
                 limit(10).dicts())

        return self.to_json(self.to_list(query))


    def to_list(self, data):
        listt = []

        for t in data:
            listt.append(t)
        return listt

    def to_json(self, dict):
        my_json = json.dumps(dict, sort_keys=True, indent=4)
        print(my_json)




print(testCon().get_data())

