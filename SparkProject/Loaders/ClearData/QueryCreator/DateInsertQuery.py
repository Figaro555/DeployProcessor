class DateInsertQuery:
    def create_query(self, date_id, day, month, year):
        return "INSERT INTO date11 (id, day, month, year)\n" + \
               "VALUES ('" + date_id + "', " + str(day) + "," + str(month) + \
               ", " + str(year) + ")"
