#
import pandas as pd
from datetime import datetime
from dateutil import parser


# 1.  Write a Pandas program to create Date Time Obj
def create_date_time_from_str(datetime_str):
    return parser.parse(datetime_str)


def create_date_time(year, month, day, hour=False, minute=False, second=False):
    if hour:
        return datetime(year, month, day, hour)
    elif hour and minute:
        return datetime(year, month, day, hour, minute)
    elif hour and minute and second:
        return datetime(year, month, day, hour, minute, second)
    return datetime(year, month, day)


def get_local_date_time():
    return datetime.now()


def get_date_from_str(datetime_str):
    return parser.parse(datetime_str).date()
    #return datetime.date(parser.parse(datetime_str))


def get_current_date():
    return get_local_date_time().date()


def get_time_from_date_time(datetime_obj):
    return datetime.time(datetime_obj)


def get_current_local_time():
    return datetime.now().time()


# 2 Write a Pandas program to print the day after and before a specified date.
# Also print the days between two given dates.
def get_after_and_before_date(date_obj):
    after = date_obj - pd.Timedelta(days=1)
    before = date_obj + pd.Timedelta(days=1)
    rng = pd.date_range(after.date(), before.date())
    return "\nOne Day Before: " + str(after) + "\nOne Day After: " + str(before) + "\n range: \n" + str(rng)


# 3 Write a Pandas program to create a date from a given year, month, day and another date from a given string format.
def get_date(year, month, day, date_str):
    date_time = datetime(year, month, day)
    date_time_s = create_date_time_from_str(date_str)
    return "\nDate 1: " + str(date_time) + "\nDate 2: "+str(date_time_s)


# 4 Write a Pandas program to create a date range using a startpoint date and a number of periods.
def get_date_range_with_start_n_period(start_date, period):
    return pd.date_range(start_date, periods=period)


# 5 Write a Pandas program to create a time series using three months frequency.
def get_data_with_frequency(start_date, frequency):
    return pd.date_range(start_date, '2000-12-01', freq=frequency)


def main():
    # 1. a) Datetime object for Jan 15 2012.
    print("1. a) Datetime object for Jan 15 2012 \n", create_date_time_from_str("Jan 15 2012"), "\n")
    print("1. a) Datetime object for Jan 15 2012 \n",create_date_time(2012, 1, 15), "\n")

    # 1. b) Specific date and time of 9:20 pm.
    print("1. b) Specific date and time of 9:20 pm \n", create_date_time_from_str("Jan 15 2012 9:20 pm"), "\n")
    print("1. b) Specific date and time of 9:20 pm \n", create_date_time(2012, 1, 15, 9, 20), "\n")

    # 1. c) Local date and time.
    print("1. c) Local date and time. \n", get_local_date_time(), "\n")

    # 1. d) A date without time.
    print("1. d) A date without time \n", get_date_from_str("Jan 15 2012 9:20 pm"), "\n")

    # 1. e) Current date.
    print("1. e) Current date \n", get_current_date(), "\n")

    # 1. f) Time from a datetime.
    datetime_obj = datetime(2021, 12, 8, 9, 48, 51)
    print("1. f) Time from a datetime\n", get_time_from_date_time(datetime_obj), "\n")

    # 1. g) Current local time.
    print("1. g) Current local time \n", get_current_local_time(), "\n")

    # 2
    print("#2", get_after_and_before_date(datetime(2001, 1, 7)), "\n")

    # 3
    print("#3", get_date(2021, 1, 15, "Jan 15 2012"), "\n")

    # 4
    print("#4 \n", get_date_range_with_start_n_period('2012-04-01', 10))

    # 5
    print("#5 \n", get_data_with_frequency('2021-01-01', '3M'), "\n")

    # a = datetime(2017, 11, 28, 23, 55, 59, 342380)
    # print("year =", a.year)
    # print("month =", a.month)
    # print("hour =", a.hour)
    # print("minute =", a.minute)
    # print("timestamp =", a.timestamp())

    # t1 = date(year=2018, month=7, day=12)
    # t2 = date(year=2017, month=12, day=23)
    # t3 = t1 - t2
    # print("t3 =", t3)

    # date_string = "21 June, 2018"
    # print("date_string =", date_string)
    # date_object = datetime.strptime(date_string, "%d %B, %Y")
    # print("date_object =", date_object)

main()
