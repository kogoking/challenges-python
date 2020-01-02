# LEAP YEAR

def is_leap(year):
    
    # The code written below works too
    '''if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False'''

    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
        
year = int(input())
print(is_leap(year))