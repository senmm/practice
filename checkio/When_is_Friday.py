def friday(day: str) -> int:
    import datetime
    date, month, year = (int(x) for x in day.split("."))
    dt = datetime.datetime(year, month, date)
    dayofweek = dt.strftime('%a')
    if dayofweek == "Mon":
        return 4
    elif dayofweek == "Tue":
        return 3
    elif dayofweek == "Wed":
        return 2
    elif dayofweek == "Thu":
        return 1
    elif dayofweek == "Fri":
        return 0
    elif dayofweek == "Sat":
        return 6
    elif dayofweek == "Sun":
        return 5
    return 0


print("Example:")
print(friday("23.04.2018"))

assert friday("12.04.2018") == 1
assert friday("01.01.1999") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
