# Working with TimeStamps
from datetime import datetime, timedelta
import time
#import datetime
print(time.time())  # No of seconds from beginning of OS


def send_emails():
    for i in range(10000):
        pass


start = time.time()  # before function call
send_emails()
end = time.time()  # after function call
duration = end - start  # time taken
print(duration)

# earlier in the course, we used timeit module, we can use that also
# many ways to do things in programming languages


# Working with DateTimes
#import datetime
# has a module called datetime
# different ways to create a datetime object
#dt = datetime.datetime(2018, 1, 1)
# better way is to
# from datetime import datetime
dt1 = datetime.now()
# for parsing or converting a ddatetime string,useful when i/p from user or reading from a file
dt2 = datetime.strptime("2018/01/01", "%Y/%m/%d")  # Y for 4 digit  year
# converting time to datetime
dt3 = datetime.fromtimestamp(time.time())
print(dt3)

print(f"{dt1.year}/{dt1.month}")  # some methods
# opposite of strptime, datetime obj to string , will give 2018/01
print(dt1.strftime("%Y%m"))
print(dt2 > dt1)  # False


# working with time deltas
# from datetime import timedelta

dt4 = datetime(2018, 1, 1)
# we can add a timedelta object to a datetime object
# dt4 = datetime(2018, 1, 1)+timedelta(days=1,seconds=1000)
# print(dt4)
dt5 = datetime.now()
duration1 = dt5 - dt4
print(duration1)

print("days", duration1.days)
print("secs", duration1.second)
# This method represents total duration in seconds
print("seconds", duration1.total_seconds())
# no month or year methods as months and years have varying amount og time
