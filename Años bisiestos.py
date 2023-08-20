year = int(input("anno:"))
if year < 1582:
    is_leap_year = year % 4 == 0
else:
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
if is_leap_year:
    print(year, "es bisiesto")
else:
    print(year, "no es bisiesto")