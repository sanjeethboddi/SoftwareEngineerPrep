# Check the wiki for leap year logic.  https://en.wikipedia.org/wiki/Leap_year
# the Gregorian rule is that a year is a leap year if it’s divisible by 4, except century years must also be divisible by 400.



def is_leap_year(year:int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def print_message(year:int):
    print(f"year {year} is {"a" if is_leap_year(year) else "not a"} leap year")


print_message(2027)
print_message(2028)
