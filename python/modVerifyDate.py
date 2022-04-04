__author__="Mahmod Ahmad"
__date__="10/28/2020"

"""This file checks if the date is valid or not"""

from datetime import *
from calendar import *

def isValidYear(year):
    if year.isdigit() and int(year) > MINYEAR and \
       int(year) < MAXYEAR:
        return True
    return False

def isValidMonth(month):
    if month.isdigit() and int(month) >= 1 \
       and int(month) <= 12:
        return True
    return False

def isValidDate(year, month, theirDays):
    res = monthrange(year, month)
    validNumDays = res[1]
    if int(theirDays) >= 1 and int(theirDays) <= validNumDays:
        return True
    return False
