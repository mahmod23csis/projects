from datetime import date, datetime
print(date.today())
print(datetime.today())
d1 = datetime(2019, 1, 31, 9, 35, 45)
print(d1.month, d1.day, d1.year, d1.hour, d1.minute)
d2 = date(2018, 10, 1)
print(d2)
print(d2.month, d2.day, d2.year, d2.weekday())
###
d1 = date.today()
d2 = date(2019, 1, 1)
daysPassed = d1-d2
print(daysPassed.days)
d1 = datetime(2019,1,1)
d2 = datetime(2019,2,1)
diffDays = d2 - d1
print(diffDays)
###
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print("Curernt Date:", date.today())
print("5 days before today: ", dt)
###
d1Str = "October 2, 2018"
print(d1Str, end = " ")
print(datetime.strptime(d1Str, "%B %d, %Y"))
###
d3 = "Jan 1 2014 2:43PM"
print(datetime.strptime(d3, "%b %d %Y %I:%M%p"))
###
print(datetime.strftime(d2, "%B %d, %y"))
print(datetime.strftime(d2, "%A %B %d, %Y"))
###
from datetime import *
print("Current date/time: ", datetime.now())
print("Week # of year: ", date.today().strftime("%W"))
print("Weekday: ", date.today().strftime("%w"))
print("Day of year: ", date.today().strftime("%j"))
print("Day of month : ", date.today().strftime("%d"))
print("Day of week: ", date.today().strftime("%A"))
###
from calendar import *
yr = int(input("Enter year or -999 to quit: "))
while yr != -999:
    if(isleap(yr)):
        print(yr, " is a leap year")
    else:
        print(yr, " is NOT a leap year")
    yr = int(input("Enter year or -999 to quit: "))
###
dayNames = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
result = monthrange(2019, 2)
print(result)
dyNum = result[0]
print("first day of February 2019: ", dayNames[dyNum])
print("number of days in February 2019: ", result[1])
###
import os, time
def last_modified_fileinfo(filepath):
    filestat = os.stat(filepath)
    date = time.localtime((filestat.st_mtime))
    year = date[0]
    month = date[1]
    day = date[2]
    hour = date[3]
    minute = date[4]
    second = date[5]
    strYear = str(year)[0:];  
    if (month <=9): 	    strMonth = '0' + str(month)
    else: 	    strMonth = str(month)
    if (day <=9): 	    strDay = '0' + str(day)
    else: 	    strDay = str(day)
    return (strYear+"-"+strMonth+"-"+strDay+" "+str(hour) \
            +":"+str(minute)+":"+str(second))
fName = input("Enter file name: ")
print(last_modified_fileinfo(fName))