#prgm to find if the given yesr is leap year or not
# the year is multiple of 4
#the yesr is multiple of 400 but not a multiple of 100

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year=int(input("Enter the year: "))
result =  check_leap_year(year)
print(result)
