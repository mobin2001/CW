from datetime import date
from datetime import timedelta
class DataHelper:
    @classmethod
    def get_next_day(cls, date_obj):
        next_day = date_obj +timedelta(days=1)
        return next_day

today = date.today()
print(today)
tomorrow = DataHelper.get_next_day(today)
print(tomorrow)