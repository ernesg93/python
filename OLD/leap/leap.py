def leap_year(year):
    """On every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
    """
    if year%4 == 0:
        if year%100 == 0 and not year%400 == 0:
            return False
        else:
            return True
    else:
            return False

print(leap_year(2015))
print(leap_year(1970))
print(leap_year(1996))
print(leap_year(1960))
print(leap_year(2100))
print(leap_year(1900))
print(leap_year(2000))
print(leap_year(2400))
print(leap_year(1800))

print(1970&100)