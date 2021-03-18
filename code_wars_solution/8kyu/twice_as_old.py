#Your function takes two arguments:
#current father's age (years)
#current age of his son (years)
#Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

def twice_as_old(dad_years_old, son_years_old):
    return abs((son_years_old * 2) - dad_years_old)
