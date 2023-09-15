def valide_day(day):
    if day > 0 and day <= 31:
        return True
    return False
    

def valide_month(month):
    if month > 0 and month <= 12:
        return True 
    return False
    

def valide_year(year):
    if year <= 2008:
        return True
    return False


def valide_date(day, month, year):
    valiting_day = valide_day(day)
    valiting_month = valide_month(month)
    valiting_year = valide_year(year)

    if valiting_day == True and valiting_month == True and valiting_year == True:
        if month == 2:
            if day > 0 and day <= 28:
                return True 
        elif month == 2 and year % 4 == 0:
            if day > 0 and day <= 29:
                return True
        elif month == 1 and month == 3 and month == 5 and month == 7 and month == 8 and month == 10 and month == 12:
            if day > 0 and day <= 31:
                return True
        elif month == 4 and month == 6 and month == 9 and month == 11:
            if day > 0 and day <= 30:
                return True
        return False

    

day = 18
month = 2
year = 2004

print(valide_date(day, month, year))