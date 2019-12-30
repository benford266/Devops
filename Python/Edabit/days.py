from datetime import date
def day_amount(month, year):
    if month != 12:
        anwser = (date(year,month+1,1) - date(year,month,1)).days
        return anwser
    else:
        return 31

day_amount(2 ,2018)