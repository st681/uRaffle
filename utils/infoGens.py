import random
import calendar

def generateBirthday():
    year = random.randint(1980, 2000)
    month = random.randint(1, 12)
    daysInMonth = calendar.monthrange(year, month)[1]
    day = random.randint(1, daysInMonth)
    monthStr = calendar.month_name[month]
    return [day, monthStr, year]