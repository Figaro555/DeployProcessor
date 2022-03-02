import time

from DataSerilazators.AbstractDataSerializator import AbstractDataSerializator


class DateSerializator(AbstractDataSerializator):
    def serialize(self, date_id, day, month, year):
        return {"id": date_id, "day": int(day), "month": int(month), "year": int(year)}
